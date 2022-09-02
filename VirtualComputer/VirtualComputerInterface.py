from VirtualComputer.LargeMemory import _128x1_ram, _64KBx8_ram
from VirtualComputer.PrintFuncs import print_depth, cvt_int, print_hex, print_hex_long

# ram = _128x1_ram()
# ram(*cvt_int(1, 1, 1, 1, 1, 1, 1, 1, 1))
#
# print_5_depth(ram.get_all())
# print_hex(ram.get(*cvt_int(1, 1, 1, 1, 1, 1, 1)))

ram = _64KBx8_ram()
ram(*cvt_int(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1), *cvt_int(1, 1, 0, 0, 1, 1, 1, 0), True)
print_hex(ram.get(*cvt_int(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1)))
