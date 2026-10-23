# SERIALANDDES - Rating 1450

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Serialize and deserialize Binary Tree

Serialization is the technique of converting a binary tree into a sequence of symbols (such as a string or a list of values) so that it can be easily stored, transferred, or reconstructed later in its original structure.

Your task is to  **design an algorithm to serialize and deserialize a binary tree**. In this problem, the serialized representation must be a level-order (breadth-first) traversal stored as an array/list of integers, where -1 represents a null node.

The following operations must be supported:

deserialize(data): Construct a binary tree from the given serialized representation.

serialize(root): Convert the reconstructed binary tree back into the same level-order representation.

After deserializing the input and serializing it again, the output should represent the same tree structure as the original input.

## Function Declaration
### Function Name

$serialize$ – This function converts a binary tree into its serialized level-order representation.

$deserialize$ – This function reconstructs a binary tree from its serialized level-order representation.

### Parameters

For $serialize$ $root$ : The root node of the binary tree to be serialized.

For $deserialize$ $data$ : A list/array of integers representing the serialized binary tree in level-order traversal. A value of $-1$ represents a null node.

### Return Value

For $serialize$ Returns a list/array of integers representing the binary tree in level-order traversal, where a value of $-1$ is used to represent a null node. For $deserialize$ Returns the root node of the reconstructed binary tree.

### Input Format
- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input: The first line of each test case contains a single integer $n$ — the number of nodes in the binary tree. The next line contains the level-order traversal of the tree using $n$ space-separated integers. A value of -1 represents a null child (i.e., an absent node).
### Output Format

For each test case, output on a new line the  **serialized representation**  of the tree after performing:

- Deserialize the given level-order input into a binary tree, and
- Serialize the reconstructed tree again.

The output must match the chosen serialization format and must represent the same tree structure as the input.

### Constraints
- $\textbf{Number of nodes in the tree:}$ $0 \leq n \leq 10^{4}$
- $\textbf{Node values range:}$ $-1000 \leq \text{Node.val} \leq 1000$
- $\textbf{Node values will never be equal to -1:}$
- $\textbf{-1 is reserved exclusively for representing null nodes.}$
### Sample 1:
Input
Output

```
3
7
10 6 15 3 8 12 20
5
7 -1 9 -1 8
0

```

```
10 6 15 3 8 12 20
7 -1 9 -1 8

```

### Explanation:
- For the first test case after serializing and deserializing the given binary tree, the structure remains the same as the original.
- For second test case an empty left subtree and partial right subtree are handled correctly by the algorithm.
- For third test case an empty tree should serialize and deserialize to an empty structure.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T15:34:06.263Z  

```py
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

from collections import deque

def deserialize(arr):
    if not arr: 
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
        return ""
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
    
```

---

[View on CodeChef](https://www.codechef.com/problems/SERIALANDDES)