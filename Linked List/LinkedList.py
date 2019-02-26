class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        temp_node = Node(item)
        if self.head is None:
            self.head = temp_node
        else:
            temp_node.next = self.head
            self.head = temp_node

    def insert_in_beginning(self, item):
        temp_node = Node(item)
        temp_node.next = self.head
        self.head = temp_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next

    def find(self, item):
        current = self.head
        count = 0
        if current is None:
            return 'Head is None, noting to search'
        else:
            while current is not None:
                if current.item == item:
                    count += 1
                current = current.next
            return count


linkedlist = LinkedList()
items = ['Apple', 'Elderberry', 'Carambola', '‎Bilberry', 'Pineapple', 'Banana', 'Peach', 'Kiwifruit', 'Pomegranate',
         'Banana']
for i in range(len(items)):
    # add items to the linked list
    linkedlist.add(items[i])
linkedlist.display()
print('Found ', linkedlist.find('Banana'), ' items')
print('-------------')
linkedlist.insert_in_beginning('Books')
linkedlist.display()