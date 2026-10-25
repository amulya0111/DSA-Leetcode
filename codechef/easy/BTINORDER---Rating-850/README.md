# BTINORDER - Rating 850

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### InOrder Traversal

In-order traversal involves visiting the left subtree first, then the root node, and finally the right subtree.

 **Algorithm** :

- Recursively traverse the left subtree.
- Visit the root node.
- Recursively traverse the right subtree.
### Video Explanation

For example, check the Inorder traversal in the following binary tree:

### Task

Given a binary tree, print its nodes in Inorder traversal, by completing the given function.

### Input Format
- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is L if $c_i$ is left child of $p_i$, else R.
### Output Format

Output on the single line, $N$ space separated integers - its nodes in the inorder traversal of the given tree.

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
2 1 4 3 5
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T16:50:20.020Z  

```py
class Solution:
    def inOrderTraversal(self, root):
        if root is None:
            return
        
        # 1. Recursively traverse the left subtree
        self.inOrderTraversal(root.left)
        
        # 2. Visit/Print the root node
        print(root.val, end=' ')
        
        # 3. Recursively traverse the right subtree
        self.inOrderTraversal(root.right)
```

---

[View on CodeChef](https://www.codechef.com/problems/BTINORDER)