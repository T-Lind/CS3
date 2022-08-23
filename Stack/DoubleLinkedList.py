from Item import Item


class DoubleLinkedList:
    def __init__(self, value):
        self.top = Item(value=value, prev_pointer=None, next_pointer=None)

    def push(self, value):
        new_item = Item(value=value, prev_pointer=self.top, next_pointer=None)
        self.top.next_pointer = new_item
        self.top = new_item

    def push_front(self, value):
        insert_item = Item(value=value)
        first_item = self.top
        while first_item.prev_pointer is not None:
            first_item = first_item.prev_pointer
        first_item.next_pointer.prev_pointer = None
        return first_item.value

    def pop(self):
        popped_item = self.top
        if self.top.prev_pointer is not None:
            self.top = self.top.prev_pointer
            return popped_item.value

    def pop_front(self):
        first_item = self.top
        while first_item.prev_pointer is not None:
            first_item = first_item.prev_pointer
        first_item.next_pointer.prev_pointer = None
        return first_item.value

    def peek(self):
        return self.top.value

    def peek_front(self):
        first_item = self.top
        while first_item.prev_pointer is not None:
            first_item = first_item.prev_pointer
        return first_item.value

