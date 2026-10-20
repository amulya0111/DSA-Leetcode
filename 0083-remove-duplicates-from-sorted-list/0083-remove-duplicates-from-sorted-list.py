# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head 
        prev=head 
        temp=head.next
        while temp:
            if temp.val==prev.val:
                prev.next=prev.next.next
            else:
                prev=prev.next
            temp=temp.next
        return head 