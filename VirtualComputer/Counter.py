from LogicGates import _and, _not, _nor


class _edge_triggered_d_flip_flop:
    def __init__(self):
        self.last_clk = False

        self.q = False
        self.q_bar = True

    def __call__(self, data, clk):
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

        raise UserWarning(f"Tried to give an invalid input to {__name__}")


class _flip_flop_oscillator:
    def __init__(self):
        self.flip_flop = _edge_triggered_d_flip_flop()
        self.osc_state = False

    def __call__(self):
        self.osc_state = _not(self.osc_state)
        return self.flip_flop(self.flip_flop.q_bar, self.osc_state)[0]
