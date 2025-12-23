# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self,val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3=ListNode()
        head=l3
        carry=0
        while l1 is not None or  l2 is not None or carry!= 0 :
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0
            n=a+b+carry
            carry=n//10
            add=n%10
            x=ListNode(add)
            l3.next=x
            l3=l3.next
            if l1: 
                l1=l1.next
            if l2: 
                l2=l2.next
        return head.next
        