# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


def addOne(head):
    # write code here...
    # lets reverse the LL
    
    
    def reverse(head):
        prev=None
        curr=head 
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
    
    # get reversed head 
    curr=reverse(head)
    temp=curr
    s=0
    carry=1
    while temp:
        n=temp.data+carry
        s=n%10
        carry=n//10
        temp.data=s
        temp=temp.next
    curr=reverse(curr)
    if carry>0:
        prev=Node(carry)
        prev.next=curr
        curr=prev
    return curr
        
            