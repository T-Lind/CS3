from VirtualComputer.LargeMemory import _128x1_ram
from VirtualComputer.PrintFuncs import print_5_depth, cvt_int

# ram = _64x1_ram()
#
# ram(*cvt_int(1, 1, 1, 1, 1, 1, 1, 1))
# print_4_depth(ram.get_all())
# print(ram.get(*cvt_int(1, 1, 1, 1, 1, 1)))

ram = _128x1_ram()
ram(*cvt_int(1, 1, 1, 1, 1, 1, 1, 1, 1))
print_5_depth(ram.get_all())
print(ram.get(*cvt_int(1, 1, 1, 1, 1, 1, 1)))

