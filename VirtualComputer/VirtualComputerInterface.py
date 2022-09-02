# from VirtualComputer.LargeMemory import _128x1_ram, _64KBx8_ram
# from VirtualComputer.PrintFuncs import print_depth, cvt_int, print_hex, print_hex_long
#
# ram = _64KBx8_ram()
# ram(*cvt_int(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1), *cvt_int(1, 1, 1, 1, 1, 1, 1, 0), True)
# print_hex(ram.get(*cvt_int(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1)))

from Counter import _flip_flop_oscillator

osc = _flip_flop_oscillator()
print(osc())
print(osc())
print(osc())
print(osc())
print(osc())
print(osc())
