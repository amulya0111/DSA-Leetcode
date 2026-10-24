# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        ds=[]
        def view(root,level):
            if not root:
                return
            if len(ds)==level:
                ds.append(root.val)
            view(root.right,level+1)
            view(root.left,level+1)
        view(root,0)
        return ds

        