# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or (head and not head.next):
            return head
        
        dummy = ListNode(-1)
        prev, curr = dummy, head
        
        while curr and curr.next:
            first, second = curr, curr.next
            
            first.next, second.next = second.next, first
            
            prev.next = second
            
            prev, curr = first, first.next
            
        return dummy.next
            
            