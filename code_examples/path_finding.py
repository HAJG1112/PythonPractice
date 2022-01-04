class Node:
    def __init__(self, loc, _bool):

        self.left = None
        self.right = None
        self.loc = loc
        self._bool = _bool

    def insert(self, loc, _bool):
    # Compare the new value with the parent node
        if self._bool:
            if _bool == self._bool:  #if the current bool arg matches the next bool arg
                if self.right is None: # if the left node is none
                    self.right = Node(loc, _bool) #set a left node
                else:
                    self.right.insert(loc, _bool) #insert a left node

            elif _bool is False: 
                if self.left is None:
                    self.left = Node(loc, _bool)
                else:
                    self.left.insert(loc, _bool)
        else:
            self.loc = loc
            self._bool = _bool

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.loc, self._bool),
        if self.right:
            self.right.PrintTree()

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

import numpy as np
matrix = [[True, False, False, False],
         [True, True, False, False],
         [False, True, True, True]]


tup_matrix = [x for x in np.ndenumerate(matrix)]
root = Node(tup_matrix[0][0], tup_matrix[0][1])

for i in range(len(tup_matrix)):
    if i == 0:
        i+=1
    else:
        root.insert(tup_matrix[i][0], tup_matrix[i][1])

root.PrintTree()

#try and rewrite it with multiple false paths. This would test the integreity of the 
#path finding algorithm. ATM it can only find a singular real path