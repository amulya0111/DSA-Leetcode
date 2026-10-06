class Solution(object):
    def rotateRight(self, head, k):
        start = temp = head 
        count = 1

        if head is None or head.next is None:
            return head 

        while temp.next is not None:
            count += 1
            temp = temp.next

        if k % count == 0:
            return head

        insert = count - (k % count)

        while insert > 1:
            start = start.next
            insert -= 1

        prefix = start.next
        start.next = None
        temp.next = head

        return prefix