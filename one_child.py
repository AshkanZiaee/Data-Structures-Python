class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self,root):
        self.root = Node(root)

    def one_child_counter(self,node):

        if not node:
            return 0
        result = 0
        if (not node.left or not node.right) and (node.left or node.right):
            result += 1
        result += (self.one_child_counter(node.left) + self.one_child_counter(node.right))
        return result

tree = BinaryTree(5)

tree.root.left = Node(8)

tree.root.right = Node(88)

tree.root.left.left = Node(888)
tree.root.right.right = Node(8888)


#            5
#          /  \
#        8     88
#       / \     \
#     888      8888
#
print(tree.one_child_counter(tree.root))
