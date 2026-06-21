# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow=head
        fast=head
        if head.next==None:
            return True
        while fast and fast.next:            
            fast=fast.next.next                
            slow=slow.next
        if fast:
            slow=slow.next
        temp=slow.next
        prev=None
        curr=slow
        while curr:
            curr.next=prev
            prev=curr
            curr=temp
            if temp is not None:
                temp=curr.next
        p1=head
        p2=prev
        while p2:
            if p1.val!=p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True

        
        