class StackEmptyError(Exception):
    pass


class StackFullError(Exception):
    pass


class Stack:
    def __init__(self, max_size=10):
        self.items = [None] * max_size
        self.count = 0

    def is_empty(self):
        return self.items == 0

    def size(self):
        return self.count

    def is_full(self):
        return self.count == len(self.items)

    def push(self, item):
        if self.is_full():
            raise StackFullError("Stack is full, can'it push the item", item)
        self.items[self.count] = item
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise StackEmptyError("Stack is empty")

        item = self.items[self.count - 1]
        self.items[self.count - 1] = None
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise StackEmptyError("Stack is empty")
        return self.items[-1]

    def display(self):
        print(self.items)


if __name__ == '__main__':
    stack = Stack()
    l = [1, 2, 1, 1, 2, 1, 'Hello', 'Apple']
    for i in range(len(l)):
        stack.push(l[i])
    stack.display()
    stack.pop()
    stack.display()
    print(stack.peek())
