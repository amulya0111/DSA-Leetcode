'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.next = None
'''

class Solution:
    def removeDuplicates(self, head):
        temp=head
        prev=dummy=Node(0)
        while temp:
            if prev.data!=temp.data:
                prev.next=temp
                prev=temp
            temp=temp.next
            
        prev.next=None
        return dummy.next    