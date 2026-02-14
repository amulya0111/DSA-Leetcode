# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        pos=-1
        slow=head
        fast=head
        while True:
            if fast==None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        return True
        
        