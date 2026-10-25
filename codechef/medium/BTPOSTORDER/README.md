# BTPOSTORDER

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### PostOrder Traversal

Post-order traversal involves visiting the left subtree first, then the right subtree, and finally the root node. This method is useful for deleting the tree and freeing up the space, as it ensures that child nodes are processed before their respective parent nodes.

 **Algorithm** :

- Recursively traverse the left subtree.
- Recursively traverse the right subtree.
- Visit the root node and print it.
### Video Explanation

For example, check the postorder traversal of the following binary tree.

### Task

Given a binary tree, print its nodes in postorder traversal.

### Input Format
- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is L if $c_i$ is left child of $p_i$, else R.
### Output Format

Output on the single line, $N$ space separated integers - its nodes in the postorder traversal of the given tree.

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
2 4 5 3 1
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T16:57:27.268Z  

```py
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def post_order_traversal(root):
    # complete this
    if root is None:
        return
    post_order_traversal(root.left)
    
    post_order_traversal(root.right)
    
    print(root.val,end=' ')
```

---

[View on CodeChef](https://www.codechef.com/problems/BTPOSTORDER)