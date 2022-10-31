class Stack:
    def __init__(self):
        self.vals = []

    def push(self, val):
        self.vals.append(val)

    def pop(self):
        return self.vals.pop()

    def peek(self):
        return self.vals[len(self.vals)-1]

    def size(self):
        return len(self.vals)

    def isEmpty(self):
        return len(self.vals) == 0

    def __str__(self):
        return str(self.vals)


def string_decoder(encoded_string):
    bracket_stack = Stack()

    output_str =

    for i in range(len(encoded_string)):
        if
