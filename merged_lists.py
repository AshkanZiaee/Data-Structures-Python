class Node():
    def __init__(self,data,next=None):
         self.data = data
         self.next = None


class LinkedNodes():
    def __init__(self,data):
        self.start = Node(data)

    def add_lists(self,n):
        start = self.start
        new_node = Node(n)
        while start.next:
            start=start.next
        start.next = new_node

    def merge_lists(self,list2):

        first_list = self.start
        second_list = list2.start
        s = None

        if not first_list:
            return second_list
        if not second_list:
            return first_list

        if first_list and second_list == None:
            return

        if first_list and second_list != None:
            if first_list.data <= second_list.data:
                s = first_list
                first_list = s.next
            else:
                s = second_list
                second_list = s.next
            new_head = s
        while first_list and second_list != None:
            if first_list.data <= second_list.data:
                s.next = first_list
                s = first_list
                first_list = s.next
            if second_list.data <= first_list.data:
                s.next = second_list
                s = second_list
                second_list = s.next
        if first_list == None:
            s.next = second_list
        if second_list == None:
            s.next = first_list

        return new_head

    def printer(self):
        start = self.start
        while start:
            print(start.data)
            start = start.next

llist_1 = LinkedNodes(1)

llist_1.add_lists(5)
llist_1.add_lists(7)
llist_1.add_lists(9)
llist_1.add_lists(10)

llist_2 = LinkedNodes(2)

llist_2.add_lists(3)
llist_2.add_lists(4)
llist_2.add_lists(6)
llist_2.add_lists(8)

llist_1.merge_lists(llist_2)

llist_1.printer()
