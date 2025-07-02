class TreeNode:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

    def insert(self, key_value): # insert a new node in ascending order from left -> right
        if key_value < self.value: # enter the left subtree of the parent node
            if self.left is None: # check if the left subtree is empty
                self.left = TreeNode(key_value)
            else: # the left subtree is not empty
                self.left.insert(key_value)

        else: # enter the right subtree of the parent node
            if self.right is None: # check if the right subtree is empty
                self.right = TreeNode(key_value)
            else: # the right subtree is not empty
                self.right.insert(key_value)

    def preorder_traversal(self): # print root -> left -> right
        print(self.value) # print the value of the root node first
        
        if self.left: # check if the left subtree is not empty
            self.left.preorder_traversal()        
        
        if self.right: # check if the left subtree is not empty
            self.right.preorder_traversal()        

    def inorder_traversal(self): # print left -> root -> right
        if self.left: # check if the left subtree is not empty
            self.left.inorder_traversal()
        
        print(self.value) # print the value at the end of the left subtree

        if self.right: # check if the right subtree is not empty, after completing the left subtree
            self.right.inorder_traversal()

    def postorder_traversal(self): # print left -> right -> root
        if self.left: # check if the left subtree is not empty
            self.left.postorder_traversal()

        if self.right: # check if the right subtree is not empty, after completing the left subtree
            self.right.postorder_traversal()

        print(self.value) # print the value of the root node last

if __name__ == "__main__":
    tree_obj = TreeNode(17)

    tree_obj.insert(5)
    tree_obj.insert(4)
    tree_obj.insert(3)

    tree_obj.insert(23)
    tree_obj.insert(20)
    tree_obj.insert(18)

    print("\n Preorder Traversal")
    tree_obj.preorder_traversal()

    print("\n Inorder Traversal")
    tree_obj.inorder_traversal()

    print("\n Postorder Traversal")
    tree_obj.postorder_traversal()