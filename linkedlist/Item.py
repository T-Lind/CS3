class Item:
    def __init__(self, *, value, next_pointer, prev_pointer=None):
        """
        Store a value of any type with a pointer to the object before and after.
        :param value: The data to store
        :param next_pointer: the reference to the next data object
        :param prev_pointer: the reference to the prev data object
        """
        self.value = value
        self.next_pointer = next_pointer
        self.prev_pointer = prev_pointer
