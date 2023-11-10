class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        current = self.head
        for _ in range(index):
            if current.next is None:
                raise IndexError
            current = current.next
        return current.data

    def remove(self, index):
        if index == 0:
            if self.head is None:
                raise IndexError
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                if current.next is None:
                    raise IndexError
                current = current.next
            if current.next is None:
                raise IndexError
            current.next = current.next.next

    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(n - 1):
                if current.next is None:
                    raise IndexError
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


linked_list = LinkedList()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
linked_list.push(5)

for item in linked_list:
    print(item)
