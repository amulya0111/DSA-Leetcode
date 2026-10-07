# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


def deleteMiddle(head):
    if head.next is None:
        head = None
        return head 
    slow=fast=head
    while fast is not None and fast.next is not None:
        prev=slow 
        slow=slow.next
        fast=fast.next.next
    prev.next=prev.next.next
    return head 

    