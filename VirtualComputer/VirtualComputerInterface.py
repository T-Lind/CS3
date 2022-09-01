from VirtualComputer.LogicGates import _edge_d_flip_flop

# print(_8_bit_adder(True, False, False, False, True, False, True, True,
#                    False, True, False, True, False, True, False, False,
#                    subtract=False
#                          ))

ff = _edge_d_flip_flop()

print(ff(1, 0))
print(ff.get())
