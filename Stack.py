class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            print("Stack overflow")
        else:
            self.stack.append(data)

    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[len(self.stack) - 1]

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def __str__(self):
        return ' '.join([str(i) for i in self.stack])