# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def listReverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move the prev pointer forward
        current = next_node       # Move the current pointer forward
    return prev                   # New head of the reversed list