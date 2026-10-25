# BTPREORDER - Rating 550

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### PreOrder Traversal

Traversing a binary tree is involves visiting all the nodes in the tree in a specific order. The purpose of tree traversal is to access each node exactly once so that the data within the nodes can be processed. There are several methods to traverse a binary tree.

Let's learn about Pre Order traversal.

Pre-order traversal involves visiting the root node first, then recursively visiting the left subtree, and finally the right subtree.

Pseudo code:

```
void preOrder(node root) {
    if (root == null) {
        return
    }
    print(root->value)
    preOrder(root->left)
    preOrder(root->right)
}

```

### Video Explanation

For example, check the preorder traversal of the following binary tree

### Task

Given a binary tree, complete the function  *preOrderTraversal*  to print the Preorder traversal of the tree.

### Input Format
- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is L if $c_i$ is left child of $p_i$, else R.
### Output Format

Output on the single line, $N$ space separated integers - the preorder traversal of the given tree.

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
1 2 3 4 5
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T16:52:22.947Z  

```py
# class Node:
#     def __init__(self, node_value):
#         self.val = node_value
#         self.left = None
#         self.right = None

class Solution:
    def preOrderTraversal(self, root):
        # complete this

        if root is None:
            return
        
        
        # 2. Visit/Print the root node
        print(root.val, end=' ')
        # 1. Recursively traverse the left subtree
        self.preOrderTraversal(root.left)
        
        # 3. Recursively traverse the right subtree
        self.preOrderTraversal(root.right)
```

---

[View on CodeChef](https://www.codechef.com/problems/BTPREORDER)