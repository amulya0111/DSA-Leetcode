# DELMIDLL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Delete the Middle Node of a Linked List

You are given the head of a singly linked list.
Your task is to  **delete the middle node**  and return the head of the modified linked list.

The middle node of a linked list of size $N$ is the node at index $⌊N / 2⌋$ (0-based indexing), where ⌊x⌋ is the floor of $x$.

If the list contains only  **one node**, delete it and return an  **empty list**  ($NULL$).

## Function Declaration
### Function Name

$deleteMiddle$ – This function deletes the middle node of a singly linked list and returns the head of the updated list.
The middle node is defined as the node at index $⌊N / 2⌋$ using 0-based indexing, where $N$ is the number of nodes in the list.

### Parameters
- $head$ : A pointer to the head of the singly linked list.
### Return Value
- Returns the head of the modified linked list after deleting the middle node.
- Returns $NULL$ if the list becomes empty (i.e., the original list had only one node).
## Constraints
- $1 \leq N \leq 10^5$
- $0 \leq \text{Node value} \leq 9$
### Input Format
- The first line contains an integer $N$ — the number of nodes in the linked list.
- The second line contains $N$ space-separated integers representing the linked list values.
### Output Format
- Print the linked list after removing the middle node.
- If the list becomes empty, print -1.
### Sample 1:
Input
Output

```
5
10 20 30 40 50

```

```
10 20 40 50

```

### Explanation:

n = 5
middle index = floor(5/2) = 2
Delete element at index 2 -> 30 is removed

### Sample 2:
Input
Output

```
3
5 15 25

```

```
5 25

```

### Explanation:

n = 3
middle index = floor(3/2) = 1
Remove the element 15.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T05:10:41.138Z  

```py
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


def deleteMiddle(head):
    if head.next is None:
        head = None
        return head 
    slow=fast=head
    while fast is not None and fast.next is not None:
        prev=slow 
        slow=slow.next
        fast=fast.next.next
    prev.next=prev.next.next
    return head 

    
```

---

[View on CodeChef](https://www.codechef.com/problems/DELMIDLL)