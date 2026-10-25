# class Node:
#     def __init__(self, node_value):
#         self.val = node_value
#         self.left = None
#         self.right = None

class Solution:
    def preOrderTraversal(self, root):
        # complete this

        if root is None:
            return
        
        
        # 2. Visit/Print the root node
        print(root.val, end=' ')
        # 1. Recursively traverse the left subtree
        self.preOrderTraversal(root.left)
        
        # 3. Recursively traverse the right subtree
        self.preOrderTraversal(root.right)