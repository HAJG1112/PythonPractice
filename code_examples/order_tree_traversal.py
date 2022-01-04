class Node:

    def __init__(self, data):

        self.left = None   #left child node pointer
        self.right = None  #right chil node pointer
        self.data = data  #data within the current node
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data: #if the data contained is less the previous nodes data
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:   #insert to the right if old data is greater than new
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

# Preorder traversal
# Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
# Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res
root = Node(27)
root.insert(14)  #inserts node to the left of27
root.insert(35) #inserts node to the right of 27
root.insert(10)  #inserts node to the left of 14
root.insert(19) #insert node to left of 27 and right of 14
root.insert(31)
root.insert(42)
print(root.PrintTree())
print(root.inorderTraversal(root))
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))