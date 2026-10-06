"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        # 1.insert copynodes in between 
        # 2.connect random pointers 
        # 3.connect next pointer 

        '1.:'
        temp=head 
        while temp !=None:
            copynode=Node(temp.val)
            copynode.next=temp.next
            temp.next=copynode
            temp=temp.next.next
        '2.:'
        temp=head
        while temp!=None:
            if temp.random==None:
                temp.next.random=None
            else:
                temp.next.random=temp.random.next
            temp=temp.next.next
        '3.:'
        temp=head
        dummy=Node(-1)
        ans=dummy
        while temp!=None:            
            ans.next=temp.next
            temp.next=temp.next.next
            temp=temp.next
            ans=ans.next
        return dummy.next
