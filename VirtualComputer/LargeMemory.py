from VirtualComputer.LogicGates import _16x1_ram, _1_to_2_decoder, _2_to_1_selector


class _32x1_ram:
    def __init__(self):
        self.ram1 = _16x1_ram()
        self.ram2 = _16x1_ram()

    def __call__(self, a_4, a_3, a_2, a_1, a_0, data_in, write):
        do_2, do_1 = _1_to_2_decoder(a_4, data_in)

        ram_1_out = self.ram1(a_3, a_2, a_1, a_0, write, do_1)
        ram_2_out = self.ram2(a_3, a_2, a_1, a_0, write, do_2)

        return ram_2_out, ram_1_out

    def get(self, a_4, a_3, a_2, a_1, a_0):
        return _2_to_1_selector(a_4, self.ram1.get(a_3, a_2, a_1, a_0), self.ram2.get(a_3, a_2, a_1, a_0))

    def get_all(self):
        return self.ram2.get_all(), self.ram1.get_all()


class _64x1_ram:
    def __init__(self):
        self.ram1 = _32x1_ram()
        self.ram2 = _32x1_ram()

    def __call__(self, a_5, a_4, a_3, a_2, a_1, a_0, data_in, write):
        do_2, do_1 = _1_to_2_decoder(a_5, data_in)

        ram_1_out = self.ram1(a_4, a_3, a_2, a_1, a_0, write, do_1)
        ram_2_out = self.ram2(a_4, a_3, a_2, a_1, a_0, write, do_2)

        return ram_2_out, ram_1_out

    def get(self, a_5, a_4, a_3, a_2, a_1, a_0):
        return _2_to_1_selector(a_5, self.ram1.get(a_4, a_3, a_2, a_1, a_0), self.ram2.get(a_4, a_3, a_2, a_1, a_0))

    def get_all(self):
        return self.ram2.get_all(), self.ram1.get_all()


class _128x1_ram:
    def __init__(self):
        self.ram1 = _64x1_ram()
        self.ram2 = _64x1_ram()

    def __call__(self, a_6, a_5, a_4, a_3, a_2, a_1, a_0, data_in, write):
        do_2, do_1 = _1_to_2_decoder(a_6, data_in)

        ram_1_out = self.ram1(a_5, a_4, a_3, a_2, a_1, a_0, write, do_1)
        ram_2_out = self.ram2(a_5, a_4, a_3, a_2, a_1, a_0, write, do_2)

        return ram_2_out, ram_1_out

    def get(self, a_6, a_5, a_4, a_3, a_2, a_1, a_0):
        return _2_to_1_selector(a_6, self.ram1.get(a_5, a_4, a_3, a_2, a_1, a_0),
                                self.ram2.get(a_5, a_4, a_3, a_2, a_1, a_0))

    def get_all(self):
        return self.ram2.get_all(), self.ram1.get_all()

class _256x1_ram:
    def __init__(self):
        self.ram1 = _128x1_ram()
        self.ram2 = _128x1_ram()

    def __call__(self, a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0, data_in, write):
        do_2, do_1 = _1_to_2_decoder(a_7, data_in)

        ram_1_out = self.ram1(a_6, a_5, a_4, a_3, a_2, a_1, a_0, write, do_1)
        ram_2_out = self.ram2(a_6, a_5, a_4, a_3, a_2, a_1, a_0, write, do_2)

        return ram_2_out, ram_1_out

    def get(self, a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0):
        return _2_to_1_selector(a_7, self.ram1.get(a_6, a_5, a_4, a_3, a_2, a_1, a_0),
                                self.ram2.get(a_6, a_5, a_4, a_3, a_2, a_1, a_0))

    def get_all(self):
        return self.ram2.get_all(), self.ram1.get_all()

class _512x1_ram:
    def __init__(self):
        self.ram1 = _256x1_ram()
        self.ram2 = _256x1_ram()

    def __call__(self, a_8, a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0, data_in, write):
        do_2, do_1 = _1_to_2_decoder(a_8, data_in)

        ram_1_out = self.ram1(a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0, write, do_1)
        ram_2_out = self.ram2(a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0, write, do_2)

        return ram_2_out, ram_1_out

    def get(self, a_8, a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0):
        return _2_to_1_selector(a_8, self.ram1.get(a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0),
                                self.ram2.get(a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0))

    def get_all(self):
        return self.ram2.get_all(), self.ram1.get_all()

class _1024x1_ram:
    def __init__(self):
        self.ram1 = _512x1_ram()
        self.ram2 = _512x1_ram()

    def __call__(self, a_9, a_8, a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0, data_in, write):
        do_2, do_1 = _1_to_2_decoder(a_9, data_in)

        ram_1_out = self.ram1(a_8, a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0, write, do_1)
        ram_2_out = self.ram2(a_8, a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0, write, do_2)

        return ram_2_out, ram_1_out

    def get(self, a_9, a_8, a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0):
        return _2_to_1_selector(a_9, self.ram1.get(a_8, a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0),
                                self.ram2.get(a_8, a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0))

    def get_all(self):
        return self.ram2.get_all(), self.ram1.get_all()
