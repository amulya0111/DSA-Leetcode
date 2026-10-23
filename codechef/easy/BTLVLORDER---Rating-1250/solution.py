# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: Node):
        if not root:
            return []
        q=deque([root])
        ans=[]
        while q:
            node=q.popleft()
            ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print(" ".join(map(str,ans)))