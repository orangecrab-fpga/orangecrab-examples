
from migen import *

from litex.soc.interconnect.csr import AutoCSR, CSRStorage, CSRField

class PWM(Module):
    def __init__(self, bitwidth, tick, offset):
        self.out = pwm = Signal(1)
        pwm_counter = Signal(bitwidth)
        counter_value = Signal(8)
        counter = Signal(16)

        # Sine Modulation
        self.specials.mem = Memory(16, 256, init=self.gen_gamma_table(256))
        p = self.mem.get_port()
        self.specials += p
        self.comb += p.adr.eq(counter_value)
        self.comb += counter.eq(p.dat_r)
        
        self.sync += [
            If(tick,
                counter_value.eq(counter_value + 1)
            )
        ]

        self.comb += pwm.eq(pwm_counter < counter)
        self.sync += pwm_counter.eq(pwm_counter + 1)

    def gen_gamma_table(self, n):
        from math import sin,pi
        return [int(0x7FFF * (sin(((2*pi) / 255.0) * i) + 1.0)) for i in range(n)]

class PDM(Module):
    def __init__(self, width=16):
        self.level = level = Signal(8)
        level_corr = Signal(16)
        self.out = out = Signal(1)

        # Gamma correction
        self.specials.mem = Memory(16, 256, init=self.gen_gamma_table(256))
        p = self.mem.get_port()
        self.specials += p
        self.comb += p.adr.eq(level)
        self.comb += level_corr.eq(p.dat_r)
        
        sigma = Signal(width+1)

        self.comb += out.eq(sigma[width])
        self.sync += sigma.eq(sigma + Cat(level_corr, out, out))

    def gen_gamma_table(self, n):
        gamma = 1.5
        return [int(0xFFFF * pow((1.0 / 255.0) * i, gamma)) for i in range(n)]

class RGB(Module, AutoCSR):
    def __init__(self, rgb_pins):
        

        self.r = CSRStorage(8, reset=255)
        self.g = CSRStorage(8)
        self.b = CSRStorage(8)


        self._div_m = CSRStorage(32)

        self._config = CSRStorage(1, fields=[
            CSRField('breath', size=1, description='Modulate output with a breath effect'),
            CSRField('rainbow', size=1, description='Modulate output with rainbow'),
        ])

        div_m_counter = Signal(32)
        strobe = Signal()

        self.sync += [
            If(div_m_counter >= self._div_m.storage,
                div_m_counter.eq(0),
            ).Else(
                div_m_counter.eq(div_m_counter + 1)
            )
        ]

        # Activate strobe on counter rollover if counter is enabled.
        self.comb += strobe.eq((div_m_counter == 0) & (self._div_m.storage != 0))

        self.submodules.pdm_r = PDM(16)
        self.submodules.pdm_g = PDM(16)
        self.submodules.pdm_b = PDM(16)
    
        self.submodules.pwm0 = PWM(16, strobe, 1 << 0)

        modulate = Signal()
        self.comb += modulate.eq(Mux(self._config.fields.breath, self.pwm0.out, 1))

        self.comb += [
            rgb_pins.r.eq(~(self.pdm_r.out & modulate)),
            rgb_pins.g.eq(~(self.pdm_g.out & modulate)),
            rgb_pins.b.eq(~(self.pdm_b.out & modulate)),
        ]

        self.comb += [
            self.pdm_r.level.eq(self.r.storage),
            self.pdm_g.level.eq(self.g.storage),
            self.pdm_b.level.eq(self.b.storage)
        ]