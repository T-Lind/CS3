from VirtualComputer.LogicGates import cvt_int
from VirtualComputer.LargeMemory import _32x1_ram, _64x1_ram
from VirtualComputer.PrintFuncs import print_4_depth

# ram = _16x1_ram()
# print_hl_bytes(ram(False, False, True, True, True, True))
# print_hl_bytes(ram(*cvt_int(1, 1, 1, 1, 1, 1)))
# print(ram.get(*cvt_int(0, 0, 1, 1)))

# ram = _16x4_ram()
# print_multi_bytes(ram(*cvt_int(1, 1, 1, 1, 1, 0, 1, 0, 1)))

ram = _64x1_ram()

ram(*cvt_int(1, 1, 1, 1, 1, 1, 1, 1))
print_4_depth(ram.get_all())
print(ram.get(*cvt_int(1, 1, 1, 1, 1, 1)))
