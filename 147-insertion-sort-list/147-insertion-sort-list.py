# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from bisect import insort

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        
        while head:
            insort(res, head.val)
            
            head = head.next
            
        dummy = ListNode(-1)
        node = dummy
        
        while res:
            node.next = ListNode(res.pop(0))
            node = node.next
            
        return dummy.next
        