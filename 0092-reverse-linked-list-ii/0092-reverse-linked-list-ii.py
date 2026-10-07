# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left==right:
            return head 
        dummy=ListNode(-1)
        dummy.next=head 
        prev=dummy 
        for i in range(left-1):
            prev=prev.next
        rev_tail=prev.next
        curr=rev_tail
        prev_rev=None
        for i in range(right-left+1):
            next_temp=curr.next
            curr.next=prev_rev
            prev_rev=curr
            curr=next_temp
        prev.next=prev_rev
        rev_tail.next=curr
        curr=dummy.next
        return curr
        