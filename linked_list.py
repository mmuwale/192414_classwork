class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval # data value of the node
        self.nextval = None # pointer to the next node
    
class SLinkedList: # singly linked list
    def __init__(self):
        self.headval = None # first node of the linked list
    
    def listprint(self): # traverse the linked list
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBeginning(self,newdata): # inserting at the beginning of a linked list
        newNode = Node(newdata)
        # Update the new nodes next val to existing node
        newNode.nextval = self.headval 
        self.headval = newNode

    def AtEnd(self,newdata): # inserting at the end of a linked list
        newNode = Node(newdata)
        if self.headval is None: # if linked list is empty
            self.headval = newNode # make new node as head
            return
        lastNode = self.headval # traverse to the last node
        while lastNode.nextval:
            lastNode = lastNode.nextval
        lastNode.nextval = newNode # change the next of the last node

    def InBetween(self, prevNode, newdata): # inserting in between 2 nodes within a linked list
        if prevNode is None:
            print("The given previous node cannot be NULL.")
            return
        newNode = Node(newdata)
        newNode.nextval = prevNode.nextval
        prevNode.nextval = newNode
    
    def RemoveNode(self, Removekey): # removing a node from the middle of a linked list
        current = self.headval # let current variable point to the head node
        if current is not None: # there is only one node
            if current.dataval == Removekey:
                self.headval = current.nextval
                return
            while current is not None:
                if current.dataval == Removekey:
                    break
                prev = current # keep track of the previous node
                current = current.nextval
            prev.nextval = current.nextval # let the previous node point to the node after next node

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

# Insert new node at the beginning
list.AtBeginning("Sun")

# Insert new node at the end
list.AtEnd("Thu")

# Insert new node in between
list.InBetween(list.headval.nextval, "Sat")

# Traverse the linked list
list.listprint()

# Remove a node from the linked list
list.RemoveNode("Wed")

