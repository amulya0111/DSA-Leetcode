# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def post_order_traversal(root):
    # complete this
    if root is None:
        return
    post_order_traversal(root.left)
    
    post_order_traversal(root.right)
    
    print(root.val,end=' ')