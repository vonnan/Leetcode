# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        level = -1
        dummy.next = head
        node = dummy
        while node:
            node = node.next
            level += 1
        
        node = dummy
        level -= n
        while level:
            node = node.next
            level -= 1
        
        node.next = node.next.next
        
        return dummy.next
            
            
