from VirtualComputer.LogicGates import print_hl_bytes, _16x1_ram, cvt_int, _16x4_ram, print_multi_bytes

# ram = _16x1_ram()
# print_byte_stacks(ram(False, False, True, True, True, True))
# print_hl_bytes(ram(*cvt_int(1, 1, 1, 1, 1, 1)))

ram = _16x4_ram()
print_multi_bytes(ram(*cvt_int(1, 1, 1, 1, 1, 0, 1, 0, 1)))
