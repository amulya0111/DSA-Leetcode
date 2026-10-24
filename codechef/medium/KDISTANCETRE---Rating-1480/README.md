# KDISTANCETRE - Rating 1480

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### All the Nodes at a distance of K in a Binary Tree

You are given the  **root**  of a binary tree, a  **target node**  (`TreeNode* target`), and an integer  **k**. Your task is to  **return all node values that are exactly $k$ edges away**  from the target node.

The nodes can be in any direction —  **upward or downward**  — and the answer can be returned  **in any order**.

### Function Declaration
- Function Name $distanceK$
- Parameters $root$: Pointer to the root node of the binary tree (TreeNode *). $target$: Pointer to the target node in the binary tree (TreeNode*). $k$: An integer representing the exact number of edges distance from the target node.
- Return Value Returns a vector of integers containing the values of all nodes that are exactly $k$ edges away from the target node. The order of values in the returned vector does not matter.
### Constraints
- $1 \leq \text{Number of nodes} \leq 500$
- $0 \leq \text{Node.val} \leq 500$
- All node values are $\textbf{unique}$
- $\text{target}$ is guaranteed to be one of the node values
- $0 \leq k \leq 1000$
### Input Format
- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input: The first line of each test case contains three space-separated integers: the number of nodes in the tree, the target node value, the value of $k$. The next line contains the level-order traversal of the binary tree, consisting of node values where $null$ represents a null/absent child.
### Output Format

For each test case, output on a new line all node values that are  **exactly $k$ edges away**  from the target node. The values may be printed in  **any order**.

### Sample 1:
Input
Output

```
1
11 7 2
10 5 15 2 7 null 18 null null 6 8
```

```
2 10

```

### Explanation:

```
          10
         /  \
        5    15
       / \     \
      2   7     18
         / \
        6   8

```

The nodes that are 2 edges away from node `7` are `2` and `10`.

### Sample 2:
Input
Output

```
1
3 2 1
1 2 3

```

```
1

```

### Explanation:

```
   1
  / \
 2   3

```

Nodes at distance 1 from node `2` are `1` (the parent).

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T01:35:36.271Z  

```py
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
                
                for neighbour in (node.left,node.right,parent[node]):
                    if neighbour and neighbour not in visited:
                        visited.add(neighbour)
                        q2.append(neighbour)
            level+=1
        return [node.val for node in q2]
```

---

[View on CodeChef](https://www.codechef.com/problems/KDISTANCETRE)