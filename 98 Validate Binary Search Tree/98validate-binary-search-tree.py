# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        result=[]
        return self.inorderlist(root,result)
    def inorderlist(self,root,result):
        if root is None:
            return True
        # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        result=[]
        return self.inorderlist(root,result)
    def inorderlist(self,root,result):
        if root is None:
            return True
        if not self.inorderlist(root.left, result):
            return False
        result.append(root.val)
        if len(result) > 1 and result[-1] <= result[-2]:
            return False
        if not self.inorderlist(root.right, result):
            return False
        return True