# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def next_smaller_value(self, head):
        temp=head 
        data=[]
        stack=[]
        while temp:
            data.append(temp)
            temp=temp.next
        ans=[-1]*len(data)
        for i in range(len(data)-1,-1,-1):
            while stack and stack[-1]>=data[i].val:
                stack.pop()
            ans[i]=stack[-1] if stack else -1
            stack.append(data[i].val)
            
        for i in range(len(data)):
            data[i].val=ans[i]
        return head     
            