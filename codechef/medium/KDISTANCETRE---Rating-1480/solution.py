# class TreeNode:
#     def __init__(self, val=0):
#         self.val = val
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root, target, k):
        if not root:
            return []
        parent={}
        q1=deque([root])
        
        while q1:
            node=q1.popleft()
            
            if node.left:
                parent[node.left]=node
                q1.append(node.left)
            if node.right:
                parent[node.right]=node
                q1.append(node.right)
        
        visited ={target}
        q2=deque([target])
        level=0
        
        while q2 and level<k:
            n=len(q2)
            
            for _ in range(n):
                node=q2.popleft()
                
                for neighbour in (node.left,node.right,parent.get(node)):
                    if neighbour and neighbour not in visited:
                        visited.add(neighbour)
                        q2.append(neighbour)
            level+=1
        return [node.val for node in q2]