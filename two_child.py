class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self,root):
        self.root = Node(root)

    def two_child_counter(self,node, counter=0):
        if not node:
            return 0
        result = 0
        if node.left and node.right:
            result += 1
        result += (self.two_child_counter(node.left) + self.two_child_counter(node.right))
        return result

    def insertion(self,tree,n):
        if n == tree.value:
            return
        if n < tree.value:
            if tree.left:
                self.insertion(tree.left, n)
            else:
                tree.left = Node(n)
        if n > tree.value:
            if tree.right:
                self.insertion(tree.right, n)
            else:
                tree.right = Node(n)

    def printer(self,type):
        if type == "postorder":
            return self.postorder(tree.root, "postorder traversal --> ")

    def postorder(self,start,traversal):
        # L R N
        if start:
            traversal = self.postorder(start.left,traversal)
            traversal = self.postorder(start.right,traversal)
            traversal += (str(start.value) + "--")
        return traversal

tree = BinaryTree(5)

# tree.insertion(tree.root, 3)
#
# tree.insertion(tree.root, 2)
#
# tree.insertion(tree.root, 99)
#
# tree.insertion(tree.root, 999999)

tree.root.left = Node(1)

tree.root.right = Node(2)

tree.root.left.left = Node(4)

tree.root.left.right = Node(8)

tree.root.right.right = Node(8)
tree.root.right.left = Node(8)

print(tree.printer("postorder"))

print(tree.two_child_counter(tree.root))
