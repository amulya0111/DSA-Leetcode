# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root):
        if not root:
            return 
        # first of all make a levels counting ds with the data elements 
        ds=[]
        # create a function for recursive call 
        def view(root,level):
            if len(ds)==level:
                ds.append(root.val)
            if root.right:
                view(root.right,level+1)
            if root.left:
                view(root.left,level+1)
        view(root,0)
        return ds