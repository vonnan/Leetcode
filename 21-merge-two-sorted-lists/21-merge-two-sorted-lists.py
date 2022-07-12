# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        node = dummy
        while list1 and list2:
            l1, l2 = list1.val, list2.val
            if l1 <= l2:
                node.next = ListNode(l1)
                node = node.next
                list1 = list1.next
            else:
                node.next = ListNode(l2)
                node = node.next
                list2 = list2.next
        if list1 or list2:
            lst = list1 or list2
            node.next = lst
            node = node.next
        
        return dummy.next
                
                