# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        
        level = -1
        while node:
            node = node.next
            level += 1
        
        level -= n
        node = dummy
        
        while level:
            node = node.next
            level -= 1
            
        node.next = node.next.next
        
        return dummy.next