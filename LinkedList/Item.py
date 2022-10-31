class Item:
    def __init__(self, *, value, next_pointer, prev_pointer=None):
        self.value = value
        self.next_pointer = next_pointer
        self.prev_pointer = prev_pointer
