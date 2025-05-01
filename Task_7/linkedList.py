class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


    def __init__(self):
        self.head = None
        self.tail = None

    
    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.data} ")
            current = current.next
        

    def delete(self, key):
        current = self.head
        previous = None

        while current and current.data != key:
            previous = current
            current = current.next

        if not current:
            print(f"Node with data {key} not found.")
            return

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        if current == self.tail:
            self.tail = previous

        del current