# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k<=1:
            return head 
        dummy=ListNode(-1)
        groupprev=dummy
        dummy.next=head 
        curr=head 
        while curr:
            tail=curr
            count=1
            while tail and count < k:
                tail=tail.next
                count+=1
            if not tail:
                break            
            #we would have found the new head on tail 
            nextgrp=tail.next
            tail.next=None
            prev=None
            # lets reverse using prev 
            temp=curr
            for i in range(k):
                nextnode=temp.next
                temp.next=prev
                prev=temp
                temp=nextnode
            # put reversed value in the dummy LL
            groupprev.next=prev
            # the first element in curr has become the last element
            curr.next=nextgrp
            groupprev=curr

            curr=nextgrp
        return dummy.next
        


                

        
        