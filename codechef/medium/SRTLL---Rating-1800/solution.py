import sys

# Increase recursion depth to handle large linked lists up to N = 10^5
sys.setrecursionlimit(200000)

class Solution:
    def rearrange(self, head):
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Split the list into two halves
        mid = self.get_mid(head)
        right = mid.next
        mid.next = None
        
        # Recursively sort both halves
        left_sorted = self.rearrange(head)
        right_sorted = self.rearrange(right)
        
        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)
    
    def get_mid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1, l2):
        dummy = Node(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        curr.next = l1 if l1 else l2
        return dummy.next