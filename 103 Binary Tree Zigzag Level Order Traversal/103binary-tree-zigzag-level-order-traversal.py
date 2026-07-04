# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []

        if root is None:
            return result

        queue = [root]
        level=0
        while queue:
            curr = []
            next_queue = []
            for i in range(len(queue)):
                x = queue.pop(0)
                curr.append(x.val)

                if x.left:
                    next_queue.append(x.left)

                if x.right:
                    next_queue.append(x.right)
            if level%2==0:
                result.append(curr)
            else:
                result.append(curr[::-1])
            queue = next_queue
            level+=1
        return result