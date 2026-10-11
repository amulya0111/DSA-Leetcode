class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # Phase 1: Detect the cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Phase 2: Find the starting node
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow