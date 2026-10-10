# SRTLL - Rating 1800

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Sort a linked list

You are given a linked list.
Your task is to sort the linked list in ascending order.

 **Note** :

- Input is already handled
- You only need to complete the function rearrange
### Input Format
- First-line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line of every test case contains an integer $N$ - the length of array.
- The second line of every test case contains $N$ integers - $A_1,A_2,..,A_N$ denoting the integers in the linked list.
- You don't need to read or print anything. Just complete the function sort() which takes the head of the linked list as input.
### Output Format

Return the head of the sorted linked list.

### Constraints
- $1\leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- $\sum N \leq 5 \cdot 10^5$
### Subtasks
- 30 points :$1 \leq N \leq 10^3$,$\sum N \leq 5 \cdot 10^3$
- 70 points : Original Constraints
### Sample 1:
Input
Output

```
3
1
1
3
5 2 7
4
4 1 2 2
```

```
1
2 5 7
1 2 2 4
```

### Explanation:

 **Test Case 1:**  The is only a single value in the entire linked list

 **Test Case 3:**  It is easy to see that the linked list after sorting is $[1, 2, 2, 4]$

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T01:12:41.817Z  

```py
# import sys
# sys.setrecursionlimit(200000)

class Solution:
    def rearrange(self, head):
        if not head or not head.next:
            return head

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        left = self.rearrange(head)
        right = self.rearrange(slow)

        return self.merge(left, right)

    def merge(self, left, right):
        dummy = Node(0)
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        curr.next = left if left else right

        return dummy.next
```

---

[View on CodeChef](https://www.codechef.com/problems/SRTLL)