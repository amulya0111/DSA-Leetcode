# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head=ListNode()
        temp=head
        if list1 is None and list2 is None:
            return None
        while list1 or list2:
            if list1 is None and list2 is not None:
                    temp.next=list2
                    return head.next
            elif list2 is None and list1 is not None:
                temp.next=list1
                return head.next
            else:
                if list1.val>=list2.val:
                    temp.next=list2
                    list2=list2.next
                    temp=temp.next
                elif list1.val<=list2.val:
                    temp.next=list1
                    list1=list1.next
                    temp=temp.next       
        return head.next          


        