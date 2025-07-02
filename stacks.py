# Difference between array and list is that array is fixed size and list is dynamic size

class Empty(Exception):
    # Custom exception to indicate that the stack is empty
    pass

class ArrayStack:
    # LIFO Stack implementation using a Python list as underlying storage
    def __init__(self):
        # Create an empty stack
        self._data = [] # non-public list instance
    
    def __len__(self):
        # Return the number of elements in the stack
        return len(self._data)
    
    def is_empty(self):
        # Return True if the stack is empty
        return len(self._data) == 0
    
    def push(self, e):
        # Add element e to the top of the stack
        self._data.append(e) # new item stored at end of list
    
    def top(self):
        # Return the element at the top of the stack
        if self.is_empty():
            raise Empty("Stack is empty") # raise empty exception if the stack is empty
        return self._data[-1] # the last item in the list
    
    def pop(self):
        # Remove and return the element at the top of the stack
        if self.is_empty():
            raise Empty("Stack is empty") # raise empty exception if the stack is empty
        return self._data.pop() # remove last item from list
    
S = ArrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)

class LinkedListStack:
    # LIFO Stack implementation using a linked list as underlying storage
    class _Node:
        # Lightweight, non-public class for storing a singly linked node
        __slots__ = '_element', '_next' # streamline memory usage
        
        def __init__(self, element):
            self._element = element # reference to the user's element
            self._next = None # reference to the next node in the list
    
    def __init__(self):
        # Create an empty stack
        self._head = None # reference to the head of the list
        self._size = 0 # number of elements in the stack
    
    def __len__(self):
        # Return the number of elements in the stack
        return self._size
    
    def is_empty(self):
        # Return True if the stack is empty
        return self._size == 0
    
    def push(self, e):
        # Add element e to the top of the stack
        new_node = self._Node(e)
        new_node._next = self._head
        self._head = new_node
        self._size += 1

    def top(self):
        # Return the element at the top of the stack
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element
    
    def pop(self):
        # Remove and return the element at the top of the stack
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    
s = LinkedListStack()
s.push(5)
s.push(3)
print(len(s))
print(s.pop())
print(s.is_empty())
print(s.pop())
print(s.is_empty())
s.push(7)
s.push(9)
print(s.top())
s.push(4)
print(len(s))
print(s.pop())
s.push(6)