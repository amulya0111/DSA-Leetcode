# STRANGELIST - Rating 1600

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Flatten a Linked List

Alice has a  **strange singly-linked list**. A usual singly linked-list or a  *not-strange linked list*  consist of nodes pointing to exactly one node (except for the the tail node which points to null). However, in case of a  **strange singly-linked list**, instead of pointing towards a single linked-list node, some nodes of the linked-list are pointing towards two nodes! Each node in the strange linked-list has two pointers named :

- next
- child

The “child” pointer of a node may again point towards a strange singly linked list.

Alice wants to restructure this linked-list into a  *not-strange linked list*. While doing so, she must follow the following rules.

Let  **cur**  be a node in restructured linked-list, then

- cur.next must occur after cur in the restructured linked-list.
- All the nodes (if any) which are part of cur.child linked list must occur after the node cur and before the node cur.next in the restructured linked list.
- Let cur be a node in the restructured linked-list, then cur.child must be “null”.

 **NOTE**  : Refer to sample case for a visual depiction.

### Input Format
- The first line of the input contains a single integer T - the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer $N$.
- The following $N - 1$ lines contain three space separated integers $u, v$ and $type$. If the value of $type$ is equal to 0, then the next pointer of node with value equal to $u$ points towards the node with value equal to $v$. If the value of type is equal to 1, then the child pointer of node with value equal to $u$ points towards the node with value equal to $v$.
- For C++ language, you need to:

Complete the function in the submit solution tab:

bool flatten(Node* head){... }

### Output Format

For each test case, the function you complete should return the restructured linked-list.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 2*10^5$
- It is guaranteed that the sum of $N$ over all test cases is less than or equal to $3*10^5$.
### Subtasks
- 5 points : There is at most one node whose child pointer in NOT null. All the other nodes have their child pointers as null pointer.
- 95 points : ORIGINAL CONSTRAINTS
### Sample 1:
Input
Output

```
1
9
4 7 1
1 2 0
2 3 0
6 9 0
3 6 0
2 4 1
4 8 0
6 5 1

```

```
1 2 4 7 8 3 6 5 9

```

### Explanation:

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T05:32:18.594Z  

```py
# Definition for a node.
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.child = None

def flatten(head):
    if not head:
        return head
        
    stack = []
    curr = head
    
    while curr:
        # If the current node has a child, redirect next to child and save old next
        if curr.child:
            if curr.next:
                stack.append(curr.next)
            curr.next = curr.child
            curr.child = None
            
        # If we reach the end of the current chain, pop from stack to continue
        if not curr.next and stack:
            curr.next = stack.pop()
            
        curr = curr.next
        
    return head
```

---

[View on CodeChef](https://www.codechef.com/problems/STRANGELIST)