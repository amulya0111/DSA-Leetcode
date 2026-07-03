# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result=[]
        return self.rinorder(root,result)
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.val)
            self.rinorder(root.right,result)
        return result