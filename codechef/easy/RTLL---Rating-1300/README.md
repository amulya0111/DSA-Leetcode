# RTLL - Rating 1300

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Reverse a Linked List

The Chef gives you a singly linked list $A$ integers and ask you to help him reverse the list.

Complete the function "listReverse" in the code snippet that takes a single argument: head of the linked list.

### Input Format
- The first line contains an integer $N$ - representing the number of elements of the linked list.
- The second line contains $N$ integers - representing the elements of the linked list.
### Output Format

For each testcase, output will be in a single line containing a list returned by the function listReverse.

### Constraints
- $1 \leq N \leq 10^5$
- $-10^9 \leq$ Node->value $\leq 10^9$
### Sample 1:
Input
Output

```
5
1 2 3 4 5
```

```
5 4 3 2 1
```

### Sample 2:
Input
Output

```
5
1 1 3 2 1
```

```
1 2 3 1 1
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-24T18:03:13.913Z  

```py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def listReverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move the prev pointer forward
        current = next_node       # Move the current pointer forward
    return prev                   # New head of the reversed list
```

---

[View on CodeChef](https://www.codechef.com/problems/RTLL)