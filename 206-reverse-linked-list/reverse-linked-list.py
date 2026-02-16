# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head 
        else:       
            prev = None
            curr = head
            nexttemp = curr.next
            while True:
                curr.next=prev
                prev = curr
                curr = nexttemp
                nexttemp = curr.next
                if curr.next is None:
                    curr.next=prev
                    prev = curr
                    return prev
            
