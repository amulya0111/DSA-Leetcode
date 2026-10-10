#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.prev = None
#        self.next = None
def findPairs(head, tail, target):
    # write code here...
    result=[]
    temp=head 
    # find last node 
    right=tail
    left=head
    while left and right and left.data < right.data:
        s=left.data+right.data
        if s<target:
            left=left.next
        elif s>target:
            right=right.prev
        else:
            result.append(f" [{left.data},{right.data}]")
            left=left.next
            right=right.prev
    if not result:
        print("[]")
    else:
        print(" ".join(result))
        
        
        