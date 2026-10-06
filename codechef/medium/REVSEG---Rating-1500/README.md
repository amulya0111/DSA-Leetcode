# REVSEG - Rating 1500

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Reverse the Segment

You are given the head of a singly linked list $A$ of length $N$. The values in the list are $A_1, A_2, \ldots, A_N$ respectively. You are also given two integers $L$ and $R$. You need to reverse the nodes of the list from position $L$ to position $R$.

#### Function Description

You are given a function named  **`reverseSegment`**  that you must complete.

The function receives the following parameters:

- head – the head pointer of a singly linked list
- L – the starting position of the segment to be reversed (1-indexed)
- R – the ending position of the segment to be reversed (1-indexed)

The linked list contains `N` nodes, and you need to reverse only the nodes from position  **L**  to  **R**, while keeping the rest of the list unchanged.

The function must  **return the head**  of the linked list  **after reversing the segment**  between positions `L` and `R`.

The input and output formats given below are only if you want to test using custom inputs

#### Constraints:
- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq L \leq R \leq N$
- $1 \leq A_i \leq 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$
### Input Format
- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N$, $L$ and $R$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
### Output Format
- For each test case, the function you complete should return the head of the list in which the nodes from the appropriate segment are reversed.
### Sample 1:
Input
Output

```
4
6 2 5
1 2 3 4 5 6
4 1 3
1 2 3 4
5 3 5
10 4 3 6 7
3 1 3
5 6 4
```

```
1 5 4 3 2 6
3 2 1 4
10 4 7 6 3
4 6 5
```

### Explanation:

 **Example case 1:**  After reversing the segment $[2,5]$ of the list, the order of the values is $1,5,4,3,2,6$.

 **Example case 2:**  After reversing the segment $[1,3]$ of the list, the order of the values is $3,2,1,4$.

 **Example case 3:**  After reversing the segment $[3,5]$ of the list, the order of the values is $10,4,7,6,3$.

 **Example case 4:**  After reversing the whole list, the order of the values is $4,6,5$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T17:03:04.477Z  

```py
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def reverseSegment(head, L, R):
    if not head or L == R:
        return head
        
    dummy = Node(-1)
    dummy.next = head 
    prev = dummy
    
    for i in range(L-1):
        prev = prev.next
        
    rev_tail = prev.next
    curr = rev_tail
    prev_rev = None
    
    for i in range(R-L+1):
        next_temp = curr.next
        curr.next = prev_rev
        prev_rev = curr
        curr = next_temp
        
    prev.next = prev_rev
    rev_tail.next = curr
    
    curr = dummy.next
    return curr
```

---

[View on CodeChef](https://www.codechef.com/problems/REVSEG)