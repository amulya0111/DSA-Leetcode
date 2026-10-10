# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

def reverse_m_size_groups(head, M):
    if not head or M <= 1:
        return head

    dummy = Node(0)
    dummy.next = head
    group_prev = dummy

    curr = head
    while curr:
        # Check if there are M nodes to reverse
        tail = curr
        count = 1
        while count < M and tail:
            tail = tail.next
            count += 1
            
        # If there are fewer than M nodes left, we don't reverse them
        if not tail:
            break
            
        next_group = tail.next
        tail.next = None # Temporarily disconnect the group

        # Reverse the current group of size M
        prev = None
        temp = curr
        for _ in range(M):
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt

        # Connect the reversed group back to the main list
        group_prev.next = prev
        curr.next = next_group

        # Move pointers for the next iteration
        group_prev = curr
        curr = next_group

    return dummy.next