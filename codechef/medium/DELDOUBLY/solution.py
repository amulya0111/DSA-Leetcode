#class Node:
#   def __init__(self, data):
#    self.data = data
#    self.next = None
#    self.prev = None



def deleteAllOccurrences(head, X):
    # write code here...
    temp=head 
    while temp:
        if temp.data==X:
            if temp==head:
                head=head.next
            else:
                p=temp.prev
                if temp.next:
                    p.next = temp.next
                    temp.next.prev=p
                else:
                    p.next=None 
        temp=temp.next
    return head 
                    