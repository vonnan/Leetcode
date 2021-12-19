# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush
from heapq import heappop
from heapq import heapify

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(lists[i].val, i) for i in range(len(lists)) if lists[i]]
        heapify(heap)
        
        head = None
        while heap:
            val, idx = heappop(heap)
            node = ListNode(val)
            if not head:
                head = node
                trav = head
            else:
                trav.next = node
                trav = trav.next
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heappush(heap, (lists[idx].val, idx))
        
        return head
                
            
        