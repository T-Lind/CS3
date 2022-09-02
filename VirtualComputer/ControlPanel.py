from VirtualComputer.LogicGates import _2_to_1_selector
from VirtualComputer.LargeMemory import _64KBx8_ram

class ControlPanel:
    def __init__(self):
        self.memory = _64KBx8_ram()

    def __call__(self, write, data_in, address, switches):
        selectors = []
        for datum_in in data_in:
            selectors.append(_2_to_1_selector())
