# Node is defined as:
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
def solve(head):
    #Return the number of critical points (integer)
    if not head.next or not head.next.next:
        return 0
    prev=head
    curr=head.next
    nextt=head.next.next
    count=0
    while nextt:
        if curr.val>prev.val and curr.val>nextt.val:
            count+=1
        
        if curr.val<prev.val and curr.val<nextt.val:
            count+=1
        prev=prev.next
        curr=curr.next
        nextt=nextt.next
    return count 
        