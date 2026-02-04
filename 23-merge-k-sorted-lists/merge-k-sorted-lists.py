# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self,start=None):
        self.start=start
    def mergeKLists(self, lists):
        # made a head node and assigned a temp
        head=ListNode()
        temp=head
        # making a while loop until the array has nothing
        # ok so instead of writing: 
        # while lists is not None:
        # we will write
        while any(lists):
         # to help continue until all lists are exhausted 
            # finding smallest
            # first initialise smallest , its a list node so:
            smallest =None
            smallest_index=-1
            for i in range(len(lists)):
                if lists[i] is not None:
                    if smallest is None or lists[i].val<smallest.val:
                        smallest = lists[i]
                        smallest_index=i
                    # found the index to be incremented , now increment pointer 
            # incrementing the list taken
            lists[smallest_index]=lists[smallest_index].next
            # assigning and incrementing temp
            # not like this: 
            # head.val=smallest
            # BECAUSE SMALLEST IS A NODE NOT VALUE
            temp.next=smallest
            temp=temp.next
        return head.next



        