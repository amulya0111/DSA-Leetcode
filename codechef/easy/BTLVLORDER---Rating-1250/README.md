# BTLVLORDER - Rating 1250

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Level Order Traversal

Given a binary tree, print the level order traversal of its nodes. (i.e., from left to right, on each level).

For example, the level order traversal of the following binary tree is:
1
2 3
4 5

### Input Format
- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is L if $c_i$ is left child of $p_i$, else R.
### Output Format

Output on the L separate lines, $N$ space separated integers - its nodes in the level order traversal of the given tree, where L is total no. of levels in the given tree.

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
2 3
4 5
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T16:33:22.583Z  

```py
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
```

---

[View on CodeChef](https://www.codechef.com/problems/BTLVLORDER)