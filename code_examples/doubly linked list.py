
# create the node in which we initialise the data for the node
# a pointer to the next node
# a pointer to the previous node

class Node:
    def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class doubly_linked_list:
    
    def __init__(self):
        self.head = None

# Adding data elements		
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

# Define the insert method to insert the element		
    def insert(self, prev_node, NewVal):
        if prev_node is None:
            return
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

# Print the Doubly Linked list		
    def listprint(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next

#remember new values are added to the front of the list!
dllist = doubly_linked_list()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.insert(dllist.head.next, 13) #this calls the next node from the first in the list, then appleis the next method again
dllist.append(45)
dllist.listprint(dllist.head)