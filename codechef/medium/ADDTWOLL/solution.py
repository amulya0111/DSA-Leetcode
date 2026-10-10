#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None
def addTwoNumbers(l1, l2):
    # write code here...
    ans=Node(0)
    temp=ans
    carry=0
    while l1 or l2 or carry:
        a=l1.data if l1 else 0
        b=l2.data if l2 else 0
        s=a+b+carry
        carry=s//10
        s=s%10
        temp.next=Node(s)
        l1=l1.next if l1 else None
        l2=l2.next if l2 else None
        temp=temp.next
    return ans.next
        