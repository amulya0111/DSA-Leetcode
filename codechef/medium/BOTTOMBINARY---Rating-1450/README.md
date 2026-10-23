# BOTTOMBINARY - Rating 1450

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Bottom view of binary tree

You are given the  **root**  of a binary tree. Your task is to return the  **bottom view**  of the tree.

The  **bottom view**  represents the set of nodes that are visible when the tree is viewed from  **below**.

For nodes that lie at the same horizontal distance from the root,  **the one appearing later in the level order traversal**  (i.e., lower in the tree) will be visible in the bottom view.

Return the nodes from  **leftmost to rightmost**.

### Function Declaration
- Function Name $bottomView$
- Parameters $root$: Pointer to the root node of the binary tree (TreeNode*).
- Return Value Returns a vector of integers representing the bottom view of the binary tree, ordered from leftmost to rightmost.
### Constraints
- $1 \leq \text{Number of Nodes} \leq 10^{4}$
- $-10^{3} \leq \text{Node.val} \leq 10^{3}$
### Input Format
- The first line contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input: The first line contains a single integer $N$ — the number of nodes in the binary tree. The second line contains $N$ space-separated values representing the level-order traversal of the tree. Use null (or -1 if preferred) to denote missing children.
### Output Format
- For each test case, output on a new line the bottom view of the binary tree.
- Print the node values from leftmost to rightmost, separated by spaces.
### Sample 1:
Input
Output

```
1
7
15 10 20 8 12 16 25
```

```
8 10 16 20 25
```

### Explanation:

Visible nodes from bottom are:
Leftmost -> 8
Then -> 10
Then -> 16 (hides 15)
Then -> 20
Then -> 25 (rightmost)

### Sample 2:
Input
Output

```
1
7
1 2 3 4 5 6 7
```

```
4 2 6 3 7
```

### Sample 3:
Input
Output

```
1
9
50 30 70 20 40 60 80 null 25
```

```
20 25 60 70 80
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T17:51:39.476Z  

```py
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

```

---

[View on CodeChef](https://www.codechef.com/problems/BOTTOMBINARY)