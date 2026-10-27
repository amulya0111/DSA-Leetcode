# Reverse Nodes in k-Group

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return  *the modified list*.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

 **Example 1:** 

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

```

 **Example 2:** 

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

```

 

 **Constraints:** 

- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

 

 **Follow-up:**  Can you solve the problem in `O(1)` extra memory space?

## Solution

**Language:** Python  
**Runtime:** 6 ms (beats 7.65%)  
**Memory:** 13.9 MB (beats 97.55%)  
**Submitted:** 2026-10-27T16:07:57.685Z  

```py
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k<=1:
            return head 
        dummy=ListNode(-1)
        groupprev=dummy
        dummy.next=head 
        curr=head 
        while curr:
            tail=curr
            count=1
            while tail and count < k:
                tail=tail.next
                count+=1
            if not tail:
                break            
            #we would have found the new head on tail 
            nextgrp=tail.next
            tail.next=None
            prev=None
            # lets reverse using prev 
            temp=curr
            for i in range(k):
                nextnode=temp.next
                temp.next=prev
                prev=temp
                temp=nextnode
            # put reversed value in the dummy LL
            groupprev.next=prev
            # the first element in curr has become the last element
            curr.next=nextgrp
            groupprev=curr

            curr=nextgrp
        return dummy.next
        


                

        
        
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/)