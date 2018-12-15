class Node(object):
    def __init__(self, item=None):
        self.data = item
        self.next = None


class Stack(object):
    def __init__(self):
        """
        default constructor
        """
        self.top = None

    def is_empty(self):
        """

        :return:
        """
        return self.top == None

    def size(self):
        """

        :return:
        """
        count = 0
        current_node = self.top
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def push(self, item):
        """

        :param item:
        :return:
        """
        temp_node = Node(item)
        temp_node.next = self.top
        self.top = temp_node

    def display(self):
        """

        :return:
        """
        if self.is_empty():
            print('Stack is empty')
            return
        current = self.top
        while current.next is not None:
            print(current.data)
            current = current.next


stack = Stack()
items = ['Apple', 'Elderberry', 'Carambola', '‎Bilberry', 'Pineapple', 'Banana', 'Peach', 'Kiwifruit', 'Pomegranate']
for i in range(len(items)):
    # add items to the Stack
    stack.push(items[i])
stack.display()
print('The size of the Stack is ', stack.size())
