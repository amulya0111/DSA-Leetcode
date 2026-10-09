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
**Submitted:** 2026-10-09T18:17:37.569Z  

```py
import sys

# Increase recursion depth to handle large linked lists up to N = 10^5
sys.setrecursionlimit(200000)

class Solution:
    def rearrange(self, head):
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Split the list into two halves
        mid = self.get_mid(head)
        right = mid.next
        mid.next = None
        
        # Recursively sort both halves
        left_sorted = self.rearrange(head)
        right_sorted = self.rearrange(right)
        
        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)
    
    def get_mid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1, l2):
        dummy = Node(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        curr.next = l1 if l1 else l2
        return dummy.next
```

---

[View on CodeChef](https://www.codechef.com/problems/SRTLL)