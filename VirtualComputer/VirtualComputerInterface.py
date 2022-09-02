# from VirtualComputer.LargeMemory import _128x1_ram, _64KBx8_ram
from VirtualComputer.PrintFuncs import print_depth, cvt_int,print_hex, print_dec, print_hex_long
#
# ram = _64KBx8_ram()
# ram(*cvt_int(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1), *cvt_int(1, 1, 1, 1, 1, 1, 1, 0), True)
# print_hex(ram.get(*cvt_int(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1)))

from Counter import _16_bit_ripple_counter, _flip_flop_oscillator
from PrintFuncs import bin_to_bools
# print(bin_to_bools(1001))
osc = _16_bit_ripple_counter()
print_hex(osc(), end=" ")
for i in range(65535):
    osc()
print_hex(osc(), end=" ")
