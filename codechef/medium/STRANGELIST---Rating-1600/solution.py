# Definition for a node.
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.child = None

def flatten(head):
    if not head:
        return head
        
    stack = []
    curr = head
    
    while curr:
        # If the current node has a child, redirect next to child and save old next
        if curr.child:
            if curr.next:
                stack.append(curr.next)
            curr.next = curr.child
            curr.child = None
            
        # If we reach the end of the current chain, pop from stack to continue
        if not curr.next and stack:
            curr.next = stack.pop()
            
        curr = curr.next
        
    return head