# BTZIGZAG - Rating 1350

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### ZigZag Traversal

Given a binary tree, print the zigzag level order traversal of its nodes. (i.e., from left to right, then right to left for the next level and alternate between).

For example, the zigzag traversal of the following binary tree is:
1
3 2
4 5

### Output Format

Output on the L separate lines, $N$ space separated integers - its nodes in the zigzag level order traversal of the given tree, where L is total no. of levels in the given tree.

### Constraints
- $1 \leq N \leq 10000$
- $1 \leq p_i, c_i \leq 100000$
- $R_i$ = L or R
- All $p_i$'s and $c_i$'s are distinct.
### Sample 1:
Input
Output

```
5
1 2 L
1 3 R
3 4 L
3 5 R

```

```
1
3 2
4 5
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T01:03:24.981Z  

```py
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
from collections import deque 

class Solution:
    def zigzag_traversal(self, root):
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

```

---

[View on CodeChef](https://www.codechef.com/problems/BTZIGZAG)