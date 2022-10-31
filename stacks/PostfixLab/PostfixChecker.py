class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[0]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

operators = "+-/*"
numbers = "123456789"

def postfix_solver(string_to_check, debug_print=False):
    num_stack = Stack()

    for character in string_to_check:
        if debug_print:
            print(num_stack)
        if character in numbers:
            num_stack.push(character)

        elif character in operators:
            num_a = num_stack.pop()
            num_b = num_stack.pop()

            num_stack.push(eval(str(num_a)+character+str(num_b)))

    return num_stack.pop()



print(postfix_solver("2 7 + 1 2 + +"))
print(postfix_solver("1 2 3 4 + + +"))
print(postfix_solver("9 3 * 8 / 4 +"))
print(postfix_solver("3 3 + 7 * 9 2 / +", True))
