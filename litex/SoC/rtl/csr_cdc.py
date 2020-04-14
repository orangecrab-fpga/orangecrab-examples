
#from migen import *
from migen import Module, Signal, Instance, ClockDomain, If
from migen.fhdl.specials import TSTriple
from migen.fhdl.decorators import ClockDomainsRenamer


#from litex.soc.interconnect.wishbone2csr import WB2CSR
from litex.soc.interconnect.csr_bus import CSRBank
from litex.soc.interconnect.csr import AutoCSR

from litex.soc.interconnect.stream import AsyncFIFO, SyncFIFO
from migen.genlib.cdc import BusSynchronizer, PulseSynchronizer, MultiReg



from litex.soc.interconnect import csr_bus, wishbone
from migen.genlib.fsm import FSM, NextState

from valentyusb.usbcore.cpu import eptri

# Custom WB2CSR that breaks out an external Ack for reads
class WB2CSR(Module):
    def __init__(self, bus_wishbone=None, bus_csr=None):
        if bus_wishbone is None:
            bus_wishbone = wishbone.Interface()
        self.wishbone = bus_wishbone
        if bus_csr is None:
            bus_csr = csr_bus.Interface()
        self.csr = bus_csr

        self.ack = Signal()
        self.en = Signal()
        

        # # #

        self.comb += [
            self.csr.dat_w.eq(self.wishbone.dat_w),
            self.wishbone.dat_r.eq(self.csr.dat_r)
        ]

        count = Signal(8)

        fsm = FSM(reset_state="WRITE-READ")
        self.submodules += fsm
        fsm.act("WRITE-READ",
            If(self.wishbone.cyc & self.wishbone.stb,
                self.csr.adr.eq(self.wishbone.adr),
                self.csr.we.eq(self.wishbone.we),
                self.en.eq(1),
                NextState("ACK"),
            )
        )
        fsm.act("ACK",
            If(self.wishbone.we | self.ack,
                self.wishbone.ack.eq(1),
                NextState("WRITE-READ")
            )
        )

from litex.soc.interconnect.csr import _make_gatherer, _CSRBase, csrprefix

class CSRClockDomainWrapper(Module):
    def get_csr(self):
        return self.usb.get_csrs()

    def __init__(self, usb_iobuf):
        self.bus = wishbone.Interface()

        # create a new custom CSR bus
        self.submodules.csr = WB2CSR(self.bus)
        csr_cpu = self.csr.csr

        self.submodules.usb = usb = ClockDomainsRenamer({'sys':'usb_12'})(eptri.TriEndpointInterface(usb_iobuf, debug=False))
        csrs = self.usb.get_csrs()
        # create a CSRBank for the eptri CSRs
        self.submodules.csr_bank = ClockDomainsRenamer({'sys':'usb_12'})(CSRBank(csrs, 0))
        csr_usb12 = self.csr_bank.bus

        if hasattr(usb, 'debug_bridge'):
            self.debug_bridge = usb.debug_bridge.wishbone
            
        # patch these two CSRs together with an Async FIFO
        _layout = [
            ("adr",    32),
            ("dat_w",   32),
            ("we", 1)
        ]

        self.submodules.fifo = fifo = ClockDomainsRenamer({'write':'sys', 'read':'usb_12'})(AsyncFIFO(_layout, 64, False))

        bus_adr = Signal(32)

        self.comb += [
            # Data into FIFO
            fifo.sink.adr.eq(csr_cpu.adr),
            fifo.sink.dat_w.eq(csr_cpu.dat_w),
            fifo.sink.we.eq(csr_cpu.we),
            fifo.sink.valid.eq(self.csr.en),

            # Always clear FIFO on clock cycle
            fifo.source.ready.eq(1),
            If(fifo.source.valid,
                csr_usb12.dat_w.eq(fifo.source.dat_w),
                csr_usb12.adr.eq(fifo.source.adr),
                bus_adr.eq(fifo.source.adr),
                csr_usb12.we.eq(fifo.source.we),
            ),
        ]

        self.submodules.fifo_r = fifo_r = ClockDomainsRenamer({'write':'usb_12', 'read':'sys'})(AsyncFIFO([("adr",    32),("dat_r",32)], 64, False))


        valid = Signal()
        source_adr = Signal(32)

        self.sync.usb_12 += [
            valid.eq(fifo.source.valid & ~csr_usb12.we),
            source_adr.eq(bus_adr)
        ]

        self.comb += [
            # Data into FIFO
            fifo_r.sink.dat_r.eq(csr_usb12.dat_r),
            fifo_r.sink.adr.eq(source_adr),
            fifo_r.sink.valid.eq(valid),
            fifo_r.source.ready.eq(1),
        ]

        self.sync += [
            self.csr.ack.eq(0),
            If(fifo_r.source.valid,
                self.csr.ack.eq(self.bus.adr[:14] == fifo_r.source.adr),
                csr_cpu.dat_r.eq(fifo_r.source.dat_r),
            ),
        ]

        # Patch interrupt through
        self.irq = Signal()
        self.specials += MultiReg(usb.ev.irq, self.irq)
        