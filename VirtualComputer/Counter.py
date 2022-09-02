from LogicGates import _and, _not, _nor, _or, _xor


class _edge_triggered_d_flip_flop:
    def __init__(self):
        self.last_clk = False

        self.q = False
        self.q_bar = True

    def __call__(self, data, clk, opp=False):
        if clk and not self.last_clk and not data:
            self.last_clk = True
            self.q, self.q_bar = False, True
            self.last_clk = clk
            return False, True

        if data and clk and not self.last_clk:
            self.q, self.q_bar = True, False
            self.last_clk = clk
            return True, False

        if not clk:
            self.last_clk = clk
            return self.q, self.q_bar

        return False, _xor(data, opp)
        # raise UserWarning(f"Tried to give an invalid input to {__name__}")


class _flip_flop_oscillator:
    def __init__(self):
        self.prev_clk = False

        self.q = False
        self.q_bar = False

    def __call__(self, data, clk):
        if data and not clk:
            self.prev_clk = clk
            self.q, self.q_bar = False, True
            return False
        if data and clk and not self.prev_clk:
            self.prev_clk = clk
            self.q, self.q_bar = True, False
            return True
        if not data and clk and not self.prev_clk:
            self.prev_clk = clk
            self.q, self.q_bar = False, True
            return False
        if not data and clk:
            self.prev_clk = clk
            self.q, self.q_bar = True, False
            return True
        if not data and not clk:
            self.prev_clk = clk
            self.q, self.q_bar = True, False
            return True
        if data and clk:
            self.prev_clk = clk
            self.q, self.q_bar = False, True
            return False
        raise Warning("Improper arguments specified into counter")


class _16_bit_ripple_counter:
    def __init__(self):
        self.ff1 = _flip_flop_oscillator()
        self.ff2 = _flip_flop_oscillator()
        self.ff3 = _flip_flop_oscillator()
        self.ff4 = _flip_flop_oscillator()
        self.ff5 = _flip_flop_oscillator()
        self.ff6 = _flip_flop_oscillator()
        self.ff7 = _flip_flop_oscillator()
        self.ff8 = _flip_flop_oscillator()
        self.ff9 = _flip_flop_oscillator()
        self.ff10 = _flip_flop_oscillator()
        self.ff11 = _flip_flop_oscillator()
        self.ff12 = _flip_flop_oscillator()
        self.ff13 = _flip_flop_oscillator()
        self.ff14 = _flip_flop_oscillator()
        self.ff15 = _flip_flop_oscillator()
        self.ff16 = _flip_flop_oscillator()

        self.clk = False

    def __call__(self):
        self.clk = _not(self.clk)

        q1 = self.ff1(self.ff1.q_bar, self.clk)
        q2 = self.ff2(self.ff2.q_bar, self.ff1.q_bar)
        q3 = self.ff3(self.ff3.q_bar, self.ff2.q_bar)
        q4 = self.ff4(self.ff4.q_bar, self.ff3.q_bar)
        q5 = self.ff5(self.ff5.q_bar, self.ff4.q_bar)
        q6 = self.ff6(self.ff6.q_bar, self.ff5.q_bar)
        q7 = self.ff7(self.ff7.q_bar, self.ff6.q_bar)
        q8 = self.ff8(self.ff8.q_bar, self.ff7.q_bar)
        q9 = self.ff9(self.ff9.q_bar, self.ff8.q_bar)
        q10 = self.ff10(self.ff10.q_bar, self.ff9.q_bar)
        q11 = self.ff11(self.ff11.q_bar, self.ff10.q_bar)
        q12 = self.ff12(self.ff12.q_bar, self.ff11.q_bar)
        q13 = self.ff13(self.ff13.q_bar, self.ff12.q_bar)
        q14 = self.ff14(self.ff14.q_bar, self.ff13.q_bar)
        q15 = self.ff15(self.ff15.q_bar, self.ff14.q_bar)

        return q15, q14, q13, q12, q11, q10, q9, q8, q7, q6, q5, q4, q3, q2, q1, _not(self.clk)


