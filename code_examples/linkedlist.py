class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval    #element
        self.nextval = None  #child

class SLinkedList:
    def __init__(self):
        self.headval = None
        self.head = None
        

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.headval
        self.head = NewNode
    # Function to add newnode

# Function to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    # Function to remove node
    def RemoveNode(self, Removekey):
        HeadVal = self.headval
        if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.head = HeadVal.nextval
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.dataval == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval

        if (HeadVal == None):
            return
        prev.next = HeadVal.nextval
        HeadVal = None

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.Atbegining("Sun")
list.AtEnd("End")
list.RemoveNode("Tue")
list.listprint()

#https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm