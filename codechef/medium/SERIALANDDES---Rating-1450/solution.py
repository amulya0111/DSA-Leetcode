# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

from collections import deque

def deserialize(arr):
    if not arr or arr[0]==-1: 
        return None
    root=TreeNode(arr[0])
    q=deque([root])
    i=1
    while q:
        node=q.popleft()
        if i<len(arr) and arr[i]!=-1:
            node.left=TreeNode(int(arr[i]))
            q.append(node.left)
        i+=1
        if i<len(arr) and arr[i]!=-1:
            node.right=TreeNode(int(arr[i]))
            q.append(node.right)
        i+=1
    return root
            
def serialize(root):
    if not root:
        return []
    q=deque([root])
    ans=[]
    while q:
        node=q.popleft()
        if node:
            ans.append(int(node.val))
            q.append(node.left)
            q.append(node.right)
        else :
            ans.append(-1)
    while ans and ans[-1]==-1:
        ans.pop()
    return ans
    