from VirtualComputer.LogicGates import _8x1_ram, _one_bit_mem

mem = _8x1_ram()
mem(True, False, True, True, True)
print(mem.get(False, True, True))
