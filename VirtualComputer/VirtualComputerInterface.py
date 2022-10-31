from virtualcomputer.LargeMemory import _64KBx8_ram
from virtualcomputer.LogicGates import _16bit_2_to_1_selector, _8_bit_latch
from virtualcomputer.PrintFuncs import print_depth, cvt_int,print_hex, print_dec, print_hex_long
# ram(*cvt_int(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1), *cvt_int(1, 1, 1, 1, 1, 1, 1, 0), True)
# print_hex(ram.get(*cvt_int(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1)))

from Counter import _16_bit_ripple_counter, _flip_flop_oscillator
from PrintFuncs import bin_to_bools
# print(bin_to_bools(1001))

osc = _16_bit_ripple_counter()
ram = _64KBx8_ram()

latch1 = _8_bit_latch()
latch2 = _8_bit_latch()
latch3 = _8_bit_latch()

# print_hex(osc(), end=" ")
# for i in range(65535):
#     osc()
# print_hex(osc(), end=" ")

select = False
write = True
data_in = (True, False, True, True, False, False, True, True)

sel = _16bit_2_to_1_selector(*osc(), *latch2.get_state(), *latch3.get_state(), select=select)

data_out = ram(*sel, *data_in, write)


