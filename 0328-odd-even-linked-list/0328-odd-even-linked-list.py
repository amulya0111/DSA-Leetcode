# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head 
        odd=head
        oddh=odd
        even=head.next
        evenh=even
        while even is not None and even.next is not None:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even = even.next
        odd.next=evenh
        return head 
            
