from VirtualComputer.LogicGates import _8x1_ram, _8x8_ram, print_bin

ram = _8x8_ram()
print(ram(True, False, True, True, True, True, True, False, True, True, True, True))
print_bin(ram.get(True, False, True))