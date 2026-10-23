# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
from collections import deque 
class Solution:
    def topView(self, root: Node):
        if not root:
            return
        q=deque([(root,0)]) #node,col
        mp={}
        mincol=0
        maxcol=0
        while q:
            node,col=q.popleft()
            if col in mp:
                continue 
            else:
                mp[col]=node.val
                mincol=min(mincol,col)
                maxcol=max(maxcol,col)
            if node.left:
                q.append((node.left,col-1))
            if node.right:
                q.append((node.right,col+1))
        ans=[mp[x] for x in range(mincol,maxcol+1)]
        print(" ".join(map(str,ans)))