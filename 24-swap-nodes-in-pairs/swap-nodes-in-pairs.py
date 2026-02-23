# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        tempo=head
        tnew=head.next
        prev=None
        while True:
            temp=tempo.next
            tempo.next=tempo.next.next
            temp.next=tempo            
            if prev is not None:
                prev.next=temp
            prev=tempo
            tempo=tempo.next
            if tempo is None or tempo.next is None:
                return tnew
            

        