# PAIRSUMDLL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Find Pairs with Given Sum in Doubly Linked List

You are given a  **sorted doubly linked list**  of  **distinct positive integers**  and an integer  **target**. Your task is to  **find all pairs**  `(a, b)` such that:

$a + b == target$ and $a < b$

Return or print all such pairs in ascending order of `a`.
If no pairs exist, print an empty list `[]`.

### Function Declaration
### Function Name

$findPairs$ – This function finds all pairs of values in a  **sorted doubly linked list**  such that:

- The sum of the pair equals the given target
- The pair satisfies $a + b = \text{target}$ and $a < b$
### Parameters
- $head$ : A pointer to the head (first node) of the doubly linked list.
- $tail$ : A pointer to the tail (last node) of the doubly linked list.
- $target$ : The integer sum for which valid pairs must be found.
### Return Value
- This function does not return a value.
- It prints all valid pairs in the format: [a, b] [c, d]... in increasing order of a.
- If no valid pairs exist, it prints [].
## Constraints
- $1 \leq N \leq 10^5$
- $1 \leq \text{Node.data} \leq 10^5$
- $1 \leq \text{target} \leq 10^5$
- The doubly linked list is sorted in strictly increasing order.
- All node values are distinct.
### Input Format
- The first line contains an integer $N$ — the number of nodes in the doubly linked list.
- The second line contains $N$ space-separated integers representing the node values in sorted order.
- The third line contains an integer $target$ — the required sum.
### Output Format
- Print all valid pairs whose sum equals target, in the format: [a, b] [c, d]...
- If no such pairs exist, print [].
### Sample 1:
Input
Output

```
7  
1 2 4 5 6 8 9  
7

```

```
[1, 6] [2, 5]

```

### Explanation:

The pairs that sum up to 7 are `(1,6)` and `(2,5)`.

### Sample 2:
Input
Output

```
3  
1 5 6  
6

```

```
[1, 5]

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:57:33.542Z  

```py
#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.prev = None
#        self.next = None
def findPairs(head, tail, target):
    # write code here...
    result=[]
    temp=head 
    # find last node 
    right=tail
    left=head
    while left and right and left.data < right.data:
        s=left.data+right.data
        if s<target:
            left=left.next
        elif s>target:
            right=right.prev
        else:
            result.append(f"[{left.data},{right.data}]")
            left=left.next
            right=right.prev
    if not result:
        print("[]")
    else:
        print(" ".join(result))
        
        
        
```

---

[View on CodeChef](https://www.codechef.com/problems/PAIRSUMDLL)