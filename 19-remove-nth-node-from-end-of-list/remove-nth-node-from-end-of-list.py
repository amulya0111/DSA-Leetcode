# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=head
        total=0
        while temp is not None:
            temp=temp.next
            total+=1
        delx=total-n
        temp=head
        count=1
        if delx==0:
            head=head.next
            return head
        while True:
            if count==delx:               
                temp.next=temp.next.next
                return head
            temp = temp.next
            count+=1
            

       
        