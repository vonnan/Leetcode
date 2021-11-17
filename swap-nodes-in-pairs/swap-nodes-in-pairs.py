# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        prev, curr = dummy, head
        
        while curr and curr.next:
            first = curr
            second = curr.next
            
            first.next = second.next
            prev.next = second
            second.next = first
            
            prev = first
            curr = first.next
        
        return dummy.next