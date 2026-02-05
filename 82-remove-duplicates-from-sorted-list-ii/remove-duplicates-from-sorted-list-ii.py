# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        # if head is None:
        #     return head
        # new= ListNode()
        # first=head
        # second = head.next
        # temp=new
        # while first is not None:
        #     if first and second:
        #         # equal
        #         if first.val==second.val:              
        #             if second.next is None:
        #                 return new.next
        #             elif second.next.val==second.val:
        #                 first=first.next
        #                 second=second.next
        #             else:
        #                 first=first.next.next
        #                 second=second.next.next
        #         # not equal
        #         elif first.val != second.val:
        #             temp.next = first
        #             temp = temp.next
        #             first=first.next
        #             second=second.next
        #         if second is None:
        #             temp.next = first
        #             temp = temp.next
        #             return new.next
        # return new.next     
        new = ListNode()
        temp=new
        current=head
        while current:
            if current.next and current.val==current.next.val:
                dupe = current.val
                while current and dupe == current.val:
                    current=current.next
            else:
                temp.next=current
                temp=temp.next
                current=current.next
        temp.next=None
        return new.next


        
        