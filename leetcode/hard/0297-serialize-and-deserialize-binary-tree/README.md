# Serialize and Deserialize Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

 **Clarification:**  The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

 **Example 1:** 

```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

```

 **Example 2:** 

```
Input: root = []
Output: []

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 104].
- -1000 <= Node.val <= 1000

## Solution

**Language:** Python  
**Runtime:** 79 ms (beats 92.85%)  
**Memory:** 22.4 MB (beats 92.44%)  
**Submitted:** 2026-10-23T14:28:08.051Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)