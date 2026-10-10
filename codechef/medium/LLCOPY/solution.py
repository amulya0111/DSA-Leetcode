def copyRandomList(head):

    if head is None:
        return None

    # Step 1: Create copy after every original node
    curr = head

    while curr is not None:
        old_next = curr.next

        copy = Node(curr.val)
        curr.next = copy
        copy.next = old_next

        curr = old_next

    # Step 2: Set random pointers
    curr = head

    while curr is not None:
        copy = curr.next

        if curr.random is not None:
            copy.random = curr.random.next

        curr = copy.next

    # Step 3: Separate the original and copied lists
    curr = head
    new_head = head.next

    while curr is not None:
        copy = curr.next

        curr.next = copy.next

        if copy.next is not None:
            copy.next = copy.next.next

        curr = curr.next

    return new_head