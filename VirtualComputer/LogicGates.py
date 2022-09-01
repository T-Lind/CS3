# Basic logic gates

def _and(a, b):
    return a & b


def _or(a, b):
    return a | b


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
            a_2), _xor(invert, a_1), _xor(invert, a_0)


def _8_bit_adder(a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0,
                 b_7, b_6, b_5, b_4, b_3, b_2, b_1, b_0,
                 subtract=False):
    b_7, b_6, b_5, b_4, b_3, b_2, b_1, b_0 = _ones_complement(b_7, b_6, b_5, b_4, b_3, b_2, b_1, b_0, subtract)

    r_7, r_6, r_5, r_4, r_3, r_2, r_1, r_0, carry_out = _8_bit_adder_basic(a_7, a_6, a_5, a_4, a_3, a_2, a_1, a_0,
                                                                           b_7, b_6, b_5, b_4, b_3, b_2, b_1, b_0,
                                                                           carry_in=subtract)

    overflow_underflow = _xor(subtract, carry_out)

    return r_7, r_6, r_5, r_4, r_3, r_2, r_1, r_0, overflow_underflow
