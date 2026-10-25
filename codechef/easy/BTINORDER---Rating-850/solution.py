class Solution:
    def inOrderTraversal(self, root):
        if root is None:
            return
        
        # 1. Recursively traverse the left subtree
        self.inOrderTraversal(root.left)
        
        # 2. Visit/Print the root node
        print(root.val, end=' ')
        
        # 3. Recursively traverse the right subtree
        self.inOrderTraversal(root.right)