class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def display(self):
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next


linkedlist = LinkedList()
items = ['Apple', 'Elderberry', 'Carambola', '‎Bilberry', 'Pineapple', 'Banana', 'Peach', 'Kiwifruit', 'Pomegranate']
for i in range(len(items)):
    # add items to the linked list
    linkedlist.add(items[i])
linkedlist.display()
