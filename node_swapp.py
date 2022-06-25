class Node():
    def __init__(self,data, next=None):
        self.data = data
        self.next = None

    def node_value(self):
        print(self.data)

class LinkedNodes():
    def __init__(self,data):
        self.start = Node(data)
        self.sizeof = 1

    def add_nodes(self, n):
        start = self.start
        new_node = Node(n)
        while start.next != None:
            start = start.next
        start.next = new_node
        self.sizeof +=1

    def swap(self, n , m):
        if n == m:
            return
        prev_1 = None
        curr_1 = self.start

        while curr_1 and curr_1.data != n:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.start

        while curr_2 and curr_2.data != m:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.start = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.start = curr_2

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def list_print(self):
        start = self.start
        while start != None:
            print(start.data, end = " ")
            start = start.next

    def last_node(self):
        start = self.start
        while start.next:
            start = start.next
        return start

my_nodes = LinkedNodes(5)

my_nodes.add_nodes(7)

my_nodes.add_nodes(8)

my_nodes.add_nodes(11)

my_nodes.add_nodes(13)

my_nodes.add_nodes(22)

my_nodes.add_nodes(78)

my_nodes.swap(22,13)

my_nodes.list_print()
