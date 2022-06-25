class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():

    def __init__(self,root):
        self.root = Node(root)


    def leaf_counter(self,node):
        if not node:
            return 0
        result = 0
        if not node.left and not node.right:
            result += 1

        result += (self.leaf_counter(node.left) + self.leaf_counter(node.right))
        return result

    def pre_order(self,start,traversal):
        # N L R
        if start:
            traversal += (str(start.value) + "--")
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal

    def traversal_printer(self,type):
        if type == "preorder":
            return self.pre_order(tree.root,"pre order traversal --> ")


    def sizee(self):
        size = 1
        my_list = []
        my_list.append(self.root)
        while my_list:
            node = my_list.pop()
            if node.left:
                size += 1
                my_list.append(node.left)
            if node.right:
                size += 1
                my_list.append(node.right)

            return size


tree = BinaryTree(8)

tree.root.left = Node(5)
tree.root.right = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left = Node(91)
tree.root.left.right = Node(92)


print(f"we have {tree.leaf_counter(tree.root)} leafs")
