# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush
from heapq import heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for lst in lists:
            while lst:
                heappush(heap, lst.val)
                lst = lst.next
        dummy = ListNode(-1)
        node = dummy
        while heap:
            node.next = ListNode(heappop(heap))
            node = node.next
        return dummy.next
                