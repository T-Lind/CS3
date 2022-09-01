# Basic logic gates

def _and(a, b):
    return a & b


def _quad_and(a, b, c, d):
    return _and(_and(a, b), _and(c, d))


def _or(a, b):
    return a | b


def _eight_or(a, b, c, d, e, f, g, h):
    first_four_or = _or(_or(a, b), _or(c, d))
    second_four_or = _or(_or(e, f), _or(g, h))
    return _or(first_four_or, second_four_or)


def _not(a):
    return not a


def _nor(a, b):
    return not _or(a, b)


def _nand(a, b):
    return not _and(a, b)


def _xor(a, b):
    return _and(_nand(a, b), _or(a, b))


# Adders

def _half_adder(a, b):
    # Returns sum out, carry out
    return _xor(a, b), _and(a, b)


def _full_adder(a, b, carry_in=False):
    """
    A full adder implemented in python using boolean staes
    :param a: A number to add
    :param b: A number to add
    :param carry_in: If a number has come in from another full adder's carry
    :return: The sum of the two numbers and carry, and the carry out
    """
    sum_1, carry_1 = _half_adder(a, b)
    sum_2, carry_2 = _half_adder(carry_in, sum_1)

    return sum_2, _or(carry_1, carry_2)


def _8_bit_adder_basic(a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0,
                       b_7, b_6, b_5, b_4, b_3, b_2, b_1, b_0,
                       carry_in=False
                       ):
    sum_0, carry_0 = _full_adder(a_0, b_0, carry_in)
    sum_1, carry_1 = _full_adder(a_1, b_1, carry_0)
    sum_2, carry_2 = _full_adder(a_2, b_2, carry_1)
    sum_3, carry_3 = _full_adder(a_3, b_3, carry_2)
    sum_4, carry_4 = _full_adder(a_4, b_4, carry_3)
    sum_5, carry_5 = _full_adder(a_5, b_5, carry_4)
    sum_6, carry_6 = _full_adder(a_6, b_6, carry_5)
    sum_7, carry_7 = _full_adder(a_7, b_7, carry_6)

    return sum_7, sum_6, sum_5, sum_4, sum_3, sum_2, sum_1, sum_0, carry_7


def _ones_complement(a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0, invert):
    return _xor(invert, a_7), _xor(invert, a_6), _xor(invert, a_5), _xor(invert, a_4), _xor(invert, a_3), _xor(invert,
                                                                                                               a_2), _xor(
        invert, a_1), _xor(invert, a_0)


def _8_bit_adder(a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0,
                 b_7, b_6, b_5, b_4, b_3, b_2, b_1, b_0,
                 subtract=False):
    b_7, b_6, b_5, b_4, b_3, b_2, b_1, b_0 = _ones_complement(b_7, b_6, b_5, b_4, b_3, b_2, b_1, b_0, subtract)

    r_7, r_6, r_5, r_4, r_3, r_2, r_1, r_0, carry_out = _8_bit_adder_basic(a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0,
                                                                           b_7, b_6, b_5, b_4, b_3, b_2, b_1, b_0,
                                                                           carry_in=subtract)

    overflow_underflow = _xor(subtract, carry_out)

    return r_7, r_6, r_5, r_4, r_3, r_2, r_1, r_0, overflow_underflow


class _r_s_flip_flop:
    def __init__(self):
        self.q = False
        self.q_bar = False

    def get_state(self):
        return self.q

    def __call__(self, r, s):
        q_bar = self.q_bar
        q = self.q
        self.q = _nor(r, q_bar)
        self.q_bar = _nor(s, q)

        return self.q, self.q_bar


class _d_type_flip_flop:
    def __init__(self):
        self.flip_flop = _r_s_flip_flop()

    def __call__(self, write, data):
        return self.flip_flop(_and(_not(data), write), _and(data, write))

    def get_state(self):
        return self.flip_flop.get_state()


class _8_bit_latch:
    def __init__(self):
        self.latch_0 = _d_type_flip_flop()
        self.latch_1 = _d_type_flip_flop()
        self.latch_2 = _d_type_flip_flop()
        self.latch_3 = _d_type_flip_flop()
        self.latch_4 = _d_type_flip_flop()
        self.latch_5 = _d_type_flip_flop()
        self.latch_6 = _d_type_flip_flop()
        self.latch_7 = _d_type_flip_flop()

    def __call__(self, d_7, d_6, d_5, d_4, d_3, d_2, d_1, d_0, write):
        return self.latch_7(write, d_7)[0], self.latch_6(write, d_6)[0], self.latch_5(write, d_5)[0], \
               self.latch_4(write, d_4)[0], \
               self.latch_3(write, d_3)[0], self.latch_2(write, d_2)[0], self.latch_1(write, d_1)[0], \
               self.latch_0(write, d_0)[0]

    def get_state(self):
        return self.latch_7.get_state(), self.latch_6.get_state(), self.latch_5.get_state(), self.latch_4.get_state(), \
               self.latch_3.get_state(), self.latch_2.get_state(), self.latch_1.get_state(), self.latch_0.get_state()


class _2_to_1_line_selector:
    def _single(self, a, b, select):
        one = _and(a, _not(select))
        two = _and(b, select)
        return _or(one, two)

    def __call__(self, a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0,
                 b_7, b_6, b_5, b_4, b_3, b_2, b_1, b_0, select
                 ):
        return self._single(a_7, b_7, select), self._single(a_6, b_6, select), self._single(a_5, b_5, select), \
               self._single(a_4, b_4, select), self._single(a_3, b_3, select), self._single(a_2, b_2, select), \
               self._single(a_1, b_1, select), self._single(a_0, b_0, select)


class _edge_d_flip_flop:
    def __init__(self):
        self.q = False
        self.q_bar = False

        self.q_mid = False
        self.q_mid_bar = False

    def __call__(self, data, clk):
        def stage_1(clock=clk):
            clock = _not(clock)

            and_1 = _and(data, clock)
            and_2 = _and(_not(data), clock)

            nor_1 = _nor(and_1, self.q_mid_bar)
            nor_2 = _nor(and_2, self.q_mid)

            self.q_mid = nor_1
            self.q_mid_bar = nor_2

        def stage_2(clock=clk):
            and_1 = _and(self.q_mid, clock)
            and_2 = _and(self.q_mid_bar, clock)

            nor_1 = _nor(and_1, self.q_bar)
            nor_2 = _nor(and_2, self.q)

            self.q = nor_1
            self.q_bar = nor_2

        # Run the first half of the flip flop
        stage_1()

        # Run the second half of the flip flop
        stage_2()

        return self.q, self.q_bar

    def get(self):
        return self.q


def _8_to_1_line_selector(s_0, s_1, s_2,
                          d_0, d_1, d_2, d_3, d_4, d_5, d_6, d_7
                          ):
    inv_s_0 = _not(s_0)
    inv_s_1 = _not(s_1)
    inv_s_2 = _not(s_2)

    and_0 = _quad_and(d_0, inv_s_0, inv_s_1, inv_s_2)
    and_1 = _quad_and(d_1, s_0, inv_s_1, inv_s_2)
    and_2 = _quad_and(d_2, inv_s_0, s_1, inv_s_2)
    and_3 = _quad_and(d_3, s_0, s_1, inv_s_2)
    and_4 = _quad_and(d_4, inv_s_0, inv_s_1, s_2)
    and_5 = _quad_and(d_5, s_0, inv_s_1, s_2)
    and_6 = _quad_and(d_6, inv_s_0, s_1, s_2)
    and_7 = _quad_and(d_7, s_0, s_1, s_2)

    return _eight_or(and_0, and_1, and_2, and_3, and_4, and_5, and_6, and_7)


def _3_to_8_decoder(s_0, s_1, s_2, data_in):
    inv_s_0 = _not(s_0)
    inv_s_1 = _not(s_1)
    inv_s_2 = _not(s_2)

    o_0 = _quad_and(data_in, inv_s_0, inv_s_1, inv_s_2)
    o_1 = _quad_and(data_in, s_0, inv_s_1, inv_s_2)
    o_2 = _quad_and(data_in, inv_s_0, s_1, inv_s_2)
    o_3 = _quad_and(data_in, s_0, s_1, inv_s_2)
    o_4 = _quad_and(data_in, inv_s_0, inv_s_1, s_2)
    o_5 = _quad_and(data_in, s_0, inv_s_1, s_2)
    o_6 = _quad_and(data_in, inv_s_0, s_1, s_2)
    o_7 = _quad_and(data_in, s_0, s_1, s_2)

    return o_7, o_6, o_5, o_4, o_3, o_2, o_1, o_0

class _8x1_ram:
    def __init__(self):
        self.bit_0 = _d_type_flip_flop()
        self.bit_1 = _d_type_flip_flop()
        self.bit_2 = _d_type_flip_flop()
        self.bit_3 = _d_type_flip_flop()
        self.bit_4 = _d_type_flip_flop()
        self.bit_5 = _d_type_flip_flop()
        self.bit_6 = _d_type_flip_flop()
        self.bit_7 = _d_type_flip_flop()

    def __call__(self, s_0, s_1, s_2, write, data_in):
        w_0, w_1, w_2, w_3, w_4, w_5, w_6, w_7 = _3_to_8_decoder(s_0, s_1, s_2, write)

        d_0 = self.bit_0(w_0, data_in)[0]
        d_1 = self.bit_1(w_1, data_in)[0]
        d_2 = self.bit_2(w_2, data_in)[0]
        d_3 = self.bit_3(w_3, data_in)[0]
        d_4 = self.bit_4(w_4, data_in)[0]
        d_5 = self.bit_5(w_5, data_in)[0]
        d_6 = self.bit_6(w_6, data_in)[0]
        d_7 = self.bit_7(w_7, data_in)[0]

        return _8_to_1_line_selector(s_0, s_1, s_2, d_0, d_1, d_2, d_3, d_4, d_5, d_6, d_7)
