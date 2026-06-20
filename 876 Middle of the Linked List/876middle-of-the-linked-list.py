# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        use slow and fast pointer 
        slow will reach the mid 
        return slow        
        """
        slow=head 
        fast=head
        if head.next is None:
            return head
        while True:
            if fast.next is None:
                return slow
            slow=slow.next
            if fast.next.next is None:
                return slow
            fast=fast.next.next

