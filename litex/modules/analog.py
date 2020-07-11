# Copyright 2020 Gregory Davill <greg.davill@gmail.com> 
# Adapted from code by Sylvain Munaut <tnt@246tNt.com> https://github.com/smunaut/ice40-playground/blob/icepick/projects/icepick_test/rtl/sense.v

from migen import *

from litex.soc.interconnect.csr import AutoCSR, CSRStorage, CSRField, CSRStatus
from litex.soc.doc.module import ModuleDoc

from litex.build.io import DDRInput

class PWM(Module):
    def __init__(self, bitwidth, tick, offset):
        ...




class AnalogSense(Module, AutoCSR, ModuleDoc):
    """Basic Analog to Digital converter.
    
    Making use of external RC circuit and FPGA differential inputs.
    An external Analog Mux is used to enable multilp channels.
    """
    def __init__(self, pads):

        charge_measurement = Signal(24)
        
        sense_mux = Signal(4)
        sense_enable_n = Signal(1)
        sense_ctrl = Signal(1)
        self.comb += [
            pads.mux.eq(sense_mux),
            pads.enable.eq(sense_enable_n),
            pads.ctrl.eq(sense_ctrl)
        ]

        # CPU interface exposed through CSRs
        self._control = CSRStorage(fields=[
            CSRField("start", size=1, offset=0, pulse=True, description="Write ``1`` to start a conversion"),
            CSRField("chan", size=4, offset=8, description="Channel selector for ADC", values= [
                        ("0b0000", "GND"),
                        ("0b0001", "A0", "analog0"),
                        ("0b0010", "A1", "analog1"),
                        ("0b0011", "A2", "analog2"),
                        ("0b0100", "A3", "analog3"),
                        ("0b0101", "A4", "analog4"),
                        ("0b0110", "A5", "analog5"),
                        ("0b0111", "AREF"),
                        ("0b1000", "3v3"),
                        ("0b1100", "1v35"),
                        ("0b1101", "2v5"),
                        ("0b1110", "1v1"),
                        ("0b1111", "VBAT"), # Through 1/2 divider
                    ]),
        ])
        self._status   = CSRStatus(fields=[
            CSRField("idle", size=1, offset=0, description="Measurement complete when read as ``1``.")
        ], description="AnalogSense Status.")
        self._result   = CSRStatus(24, description="Conversion result.")

        # FSM
        fsm = FSM(reset_state="IDLE")
        self.submodules += fsm
        timer = Signal(18)
        timer_trig = Signal()

        fsm.act("IDLE",      If(self._control.fields.start, NextState("SETUP")),   NextValue(timer, 0x18000))   # 680us
        fsm.act("SETUP",     If(timer_trig,                 NextState("CHARGE"),   NextValue(timer, 0x18000)))  # 680us
        fsm.act("CHARGE",    If(timer_trig,                 NextState("DISCHARGE"),NextValue(timer, 0x0) ))     # 2.73ms
        fsm.act("DISCHARGE", If(timer_trig,                 NextState("IDLE"))) 

        # Timers
        self.sync += timer.eq(timer + 1)
        self.comb += timer_trig.eq(timer[17])

        # Input 
        sense_iob = Signal(2)
        self.specials += DDRInput(pads.sense_p, sense_iob[0], sense_iob[1])

        sense_value = Signal(2)
        self.sync += sense_value.eq(Cat(
                sense_iob[0] ^ sense_iob[1],
                sense_iob[0] & sense_iob[1]
            ))
        
        # Measurement Counters
        sense_counter = Signal(24)
        self.sync += [
            If(timer_trig,
                sense_counter.eq(0)
            ).Else(
                sense_counter.eq(sense_counter + sense_value)
            )
        ]

        # Control Hardware
        self.sync += [
            If(fsm.ongoing("IDLE"),
                sense_mux.eq(Mux(self._control.fields.start,
                    self._control.fields.chan, 0)),
                sense_enable_n.eq(~self._control.fields.start)
            ),
            sense_ctrl.eq(fsm.ongoing("CHARGE")),
        ]

        # IF
        self.comb += [
            self._status.fields.idle.eq(fsm.ongoing("IDLE")),
            self._result.status.eq(charge_measurement)
        ]

        # Save result of charge time
        self.sync += If(fsm.ongoing("CHARGE") & timer_trig, 
                        charge_measurement.eq(sense_counter))