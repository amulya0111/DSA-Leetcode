# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque        
class Solution:
    def bottom_view(self, root):
        if not root:
            return []
        q=deque([(root,0)])
        mp={}
        mincol=0
        maxcol=0
        while q:
            node,col=q.popleft()
            mp[col]=node.val
            mincol=min(mincol,col)
            maxcol=max(maxcol,col)
            if node.left:
                q.append((node.left,col-1))
            if node.right:
                q.append((node.right,col+1))
        ans=[mp[x] for x in range(mincol,maxcol+1)]
        return ans
