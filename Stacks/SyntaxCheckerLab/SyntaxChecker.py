class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop(0)

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


class SyntaxChecker:
    def __init__(self):
        self.syntax_stack = Stack()

        self.open_symbols = '([{<'
        self.closed_symbols = ')]}>'

    def get_balanced(self, string_to_check):
        for char in string_to_check:
            if char in self.open_symbols:
                self.syntax_stack.push(char)

            elif char in self.closed_symbols:
                if not self.syntax_stack.isEmpty() \
                   and self.open_symbols[self.closed_symbols.index(char)] == self.syntax_stack.peek():
                    self.syntax_stack.pop()
                else:
                    self.syntax_stack.clear()
                    return False
        if self.syntax_stack.isEmpty():
            self.syntax_stack.clear()
            return True
        self.syntax_stack.clear()
        return False

    def __call__(self, string_to_check):
        balanced = self.get_balanced(string_to_check)
        
        if balanced:
            return string_to_check+" is correct"
        return string_to_check+" is incorrect"


checker = SyntaxChecker()
print(checker('(abc(*def)'))
print(checker('[{}]'))
print(checker('['))
print(checker('[{&lt;()&gt;}]'))
print(checker('{&lt;html[value=4]*(12)&gt;{$x}}'))
print(checker('[one]&lt;two&gt;{three}(four)'))
print(checker('car(cdr(a)(b)))'))
print(checker('car(cdr(a)(b))'))
