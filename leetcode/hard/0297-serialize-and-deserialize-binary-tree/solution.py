# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = 
#         self.right = 

from collections import deque

class Codec:

    def serialize(self, root):
        # so first of all check base 
        if not root:
            return ""
        # now we use dequeue
        q=deque([root])
        ans=[]
        while q:
            node=q.popleft()
            if node:
                ans.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                ans.append("None")
        return ",".join(ans)
    def deserialize(self, data):
        if not data:
            return None
        values=data.split(",")
        root=TreeNode(int(values[0]))
        q=deque([root])
        i=1
        while q:
            node=q.popleft()
            if values[i]!="None":
                node.left=TreeNode(int(values[i]))
                q.append(node.left)
            i+=1

            if values[i]!="None":
                node.right=TreeNode(int(values[i]))          
                q.append(node.right)
            i+=1
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))