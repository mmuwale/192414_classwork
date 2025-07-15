class Node:
    def __init__(self, data):
        self.data = data # assigns the given data to the node
        self.next = None # set the next attribute pointer to Null

class LinkedList:
      def __init__(self):
          self.head  = None
 
      def insertAtBegininning(self, new_data):
          new_node   = Node(new_data)
          new_node.next = self.head
          self.head = new_node
 
      def printList(self):
          temp = self.head  # Start from the head of the list
          while temp:
              print(temp.data, end=' ') # Print the data in the current node
              temp = temp.next # Move to the next node
          print()
 
      #Inserting a new nodwe at the end of the Lidt.
      def insertAtTheEnd(self, new_data):
          new_node  = Node(new_data)   # Create a new node
          if self.head is None:
              self.head = new_node  # If the list is empty, make the new node the head
              return
          last = self.head
          while last: # Otherwise, traverse the list to find the last node
              last = last.next
          last = new_node # Make the new node the next node of the last node
 
      def deleteFromBeginning(self):
          if self.head is None:
              return "The List is Empty"  #If empty return this string
          self.head = self.head.next   #if not empty, remove te head by making the next node the new head
 
      def deleteFromEnd(self):
          if self.head is None:
              return  "List is Empty"
          if self.head.next is None:
              self.head = None #if there's only one node, remove the head by making it none
              return
          temp = self.head
          while temp.next.next: # Otherwise, go to the second-last node
              temp = temp.next
          temp.next = None    # Remove the last node by setting the next pointer of the second-last node to None
 
  #Searching the linked list for a specific value
      def search(self, value):
          current = self.head  # Start with the head of the list
          position = 0  # Counter to keep track of the position
          while current:  # Traverse the list
              if current.data == value:  # Compare the list's data to the search value
                  return f"Value '{value}' found at position {position}"  # Print the value if a match is found
              current = current.next
              position += 1
          return f"Value '{value}' not found in the list"
 
if __name__ == '__main__':
      # Create a new LinkedList instance
      llist = LinkedList()
 
      # Insert each letter at the beginning using the method we created
      llist.insertAtBegininning('fox')
      llist.insertAtBegininning('brown')
      llist.insertAtBegininning('quick')
      llist.insertAtBegininning('the')
 
      # Now 'the' is the head of the list, followed by 'quick', then 'brown' and 'fox'
 
      # Print the list
      llist.printList()
      # Insert a word at the end
      llist.insertAtTheEnd('jumps')
 
      llist.printList()
 
      # Deleting nodes from the beginning and end
      llist.deleteFromBeginning()
      print("List after deletion:")
      llist.printList()
      # Search for 'quick' and 'lazy' in the list
      print(llist.search('quick'))  # Expected to find
      print(llist.search('lazy'))  # Expected not to find