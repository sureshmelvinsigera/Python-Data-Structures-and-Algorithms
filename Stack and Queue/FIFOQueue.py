class FIFOQueue(object):
    def __init__(self):
        self.front = self.rear = None
        self.items = []

    def eneque(self, item):
        self.items.append(item)

    def dequque(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue."
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def display(self):
        for i in range(len(self.items)):
            print(self.items[i])


if __name__ == '__main__':
    fifqueue = FIFOQueue()
    items = ['Apple', 'Elderberry', 'Carambola', '‎Bilberry', 'Pineapple', 'Banana', 'Peach', 'Kiwifruit',
             'Pomegranate']
    for i in range(len(items)):
        # add items to the linked list
        fifqueue.eneque(items[i])
    fifqueue.display()
    print("=== After dequque ===")
    fifqueue.dequque()
    fifqueue.display()
