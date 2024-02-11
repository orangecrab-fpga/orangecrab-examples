# This file is Copyright (c) Greg Davill <greg.davill@gmail.com>
# License: BSD

from migen import *

from litex.soc.interconnect.csr import AutoCSR, CSRStorage, CSRField, CSRStatus, CSRAccess
from migen.genlib.cdc import MultiReg

def io_pins():
    return Record([("i", 1),("o", 1),("oe", 1)])


class IOPin(Module):
    def __init__(self, pad):
        self.pad = pad
        self.ctrl = []
        self.alt = Signal(8, reset=0)

        self._ts = ts = TSTriple()
        self.specials += ts.get_tristate(pad)

    def add_alt(self, alt):
        self.ctrl += [alt]

    def finalize(self):
        _in = Signal()
        self.specials += MultiReg(self._ts.i, _in)
        
        # Connect up IO signals depending on alt-setting.
        for i,c in zip(range(len(self.ctrl)), self.ctrl):
            self.comb += [
                If(self.alt == i,
                    self._ts.o.eq(c.o), 
                    self._ts.oe.eq(c.oe),
                    c.eq(_in),
                )
            ]

            

class IOPort(Module, AutoCSR):
    def __init__(self, pads):
        self.alt_fields = ["csr_control"]

        pins  = [0,1,5,6,9,10,11,12,13,18,19,20,21]
        nbits = len(pins)
        fields= []
        fields_read = []


        for n in pins:
            fields += [
                CSRField(f"io{n}", 1, n ,description=f"Control for I/O pin {n}", access=CSRAccess.ReadWrite),
            ]
        for n in pins:
            fields_read += [
                CSRField(f"io{n}", 1, n ,description=f"Control for I/O pin {n}", access=CSRAccess.ReadOnly),
            ]



        self._oe  = CSRStorage(nbits, description="""GPIO Tristate(s) Control.
        Write ``1`` enable output driver""", fields=fields)
        self._in  = CSRStatus(nbits,  description="""GPIO Input(s) Status.
        Input value of IO pad as read by the FPGA""", fields=fields_read)
        self._out = CSRStorage(nbits, description="""GPIO Ouptut(s) Control.
        Value loaded into the output driver""", fields=fields)

        # # #

        self._io = []
        for n,p in zip(pins,pads):
            m = IOPin(p)

            # Create a connection to the CSR
            alt_csr = io_pins()
            self.comb += [alt_csr.o.eq(self._out.storage[n]), alt_csr.oe.eq(self._oe.storage[n]), self._in.status.eq(alt_csr.i)]
            m.add_alt(alt_csr)

            self.submodules += m
            self._io += [(n,m)]

    def finalize(self):
        # create Alt fields
        values = []
        
        for i,n in zip(range(len(self.alt_fields)), self.alt_fields):
            values += [(i,n)]

        f = CSRField("ctrl", size=8, description="Select alternative function on IO pin", values=values)

        for n,m in self._io:
            csr = CSRStorage(8, name=f"alt{n}", description="""GPIO Alt Control.
            IO pin alternative functions""", fields=[f])
            setattr(self, f"_alt{n}", csr)

            self.comb += m.alt.eq(csr.storage)

        
    def add_alt(self):
        ...