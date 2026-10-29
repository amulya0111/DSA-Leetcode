# CRITLIST - Rating 1300

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Critical points in a Linked List

Given the head of a linked list, Find the number of critical points. (The starting and end are not considered critical points).

Local minima or maxima are called critical points.

A Node is called a local minima if both next and previous elements are greater than the current element.

A Node is called a local maxima if both next and previous elements are smaller than the current element.

### Constraints
- $1 \leq$ Number of elements in the linked list, $N$ $\leq 10^5$
- $1 \leq Node.data \leq 10^9$
### Sample 1:
Input
Output

```
8
1 2 3 3 3 5 1 3

```

```
2 
```

### Explanation:

1 is a minima and 5 is a maxima hence there are 2 critical points

### Sample 2:
Input
Output

```
7
1 2 3 2 1 3 2 
```

```
3
```

### Explanation:

3rd node, 5th node and 6th node are the critical nodes, hence the answer is 3

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-29T16:58:09.587Z  

```py
# Node is defined as:
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
def solve(head):
    #Return the number of critical points (integer)
    if not head.next or not head.next.next:
        return 0
    prev=head
    curr=head.next
    nextt=head.next.next
    count=0
    while nextt:
        if curr.val>prev.val and curr.val>nextt.val:
            count+=1
        
        if curr.val<prev.val and curr.val<nextt.val:
            count+=1
        prev=prev.next
        curr=curr.next
        nextt=nextt.next
    return count 
        
```

---

[View on CodeChef](https://www.codechef.com/problems/CRITLIST)