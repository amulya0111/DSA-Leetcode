# class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


def getLength(head):
    #write your code here...
    if not head:
        return 0 
    temp=head 
    count=1
    while temp.next:
        temp=temp.next
        count+=1
    return count 