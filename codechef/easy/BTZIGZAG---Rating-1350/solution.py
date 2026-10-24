# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
from collections import deque 

class Solution:
    def zigzagTraversal(self, root):
        if not root:
            return
        q=deque([root])
        ans=[]
        
        l2r=True
        
        while q:
            n=len(q)
            row=[0]*n
            
            for i in range(n):
                node = q.popleft()
                
                if l2r:
                    index = i
                else:
                    index=n-1-i
                row[index]=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            print(*(row))
            ans.append(row)
            l2r=not l2r
            # may return thr ans but here we gotta print each row 
