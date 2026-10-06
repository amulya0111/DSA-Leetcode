"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def reverseSegment(head, L, R):
    temp=head
    if not head or L==R:
        res=[]
        curr=dummy.next
        while curr:
            res.append(str(curr.data))
            curr=curr.next
        print(" ".join(res))
        
    dummy=Node(-1)
    dummy.next=head 
    prev=dummy
    for i in range(L-1):
        prev=prev.next
    rev_tail=prev.next
    curr=rev_tail
    prev_rev=None
    
    for i in range(R-L+1):
        next_temp=curr.next
        curr.next=prev_rev
        prev_rev=curr
        curr=next_temp
    prev.next=prev_rev
    rev_tail.next=curr
    # you cant return 
    res=[]
    curr=dummy.next
    while curr:
        res.append(str(curr.data))
        curr=curr.next
    print(" ".join(res))