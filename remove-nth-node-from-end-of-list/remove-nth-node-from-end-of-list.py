# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size, node = 0, head
        while node:
            node = node.next
            size += 1
            
        size -= n
        
        start = 0
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        
        while size:
            node = node.next
            size -= 1
            
        node.next = node.next.next
        
        return dummy.next
            