# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        result = []

        if root is None:
            return result

        queue = [root]

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

            result.append(curr)
            queue = next_queue

        return result