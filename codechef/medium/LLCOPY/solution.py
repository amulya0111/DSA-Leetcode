#class Node:
#    def __init__(self, val):
#        self.val = val
#        self.next = None
#        self.random = None

def copyRandomList(head):
    if not head:
        return None

    # Step 1: Create new nodes and interleave them with the original list
    curr = head
    while curr:
        new_node = Node(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next

    # Step 2: Assign random pointers for the cloned nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate the interleaved list into original and cloned lists
    curr = head
    new_head = head.next
    copy_curr = new_head
    
    while curr:
        curr.next = curr.next.next
        if copy_curr.next:
            copy_curr.next = copy_curr.next.next
        curr = curr.next
        copy_curr = copy_curr.next

    return new_head