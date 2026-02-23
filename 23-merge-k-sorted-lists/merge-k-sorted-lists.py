# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergetwolists(self, list1, list2):
        head=ListNode()
        temp=head
        while list1 and list2:
            if list1.val>=list2.val:
                temp.next=list2
                list2=list2.next
            else:
                temp.next=list1
                list1=list1.next
            temp=temp.next
        temp.next=list1 if list1 else list2
        return head.next
    def mergeKLists(self, lists):
        if not lists:
            return None
        while len(lists) > 1: #eg: [l1,l2,l3,l4,l5]
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.mergetwolists(l1, l2)) #appending (l1+l1,l3+l4,l5+None) i.e [m1,m2,m3]
            lists = merged #i.e lists=[m1,m2,m3] and it will keep going ([m12,m3n]>[M]) until len lists is>1 , as [M] is found , it will return 
        return lists[0]
        