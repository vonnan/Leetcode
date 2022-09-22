# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        level = 0
        node = head
        while node:
            node = node.next
            level += 1
        
        if level == 1:
            return None
        
        level //= 2
        level -= 1
        
        node = head
        while level:
            node = node.next
            level -= 1
        
        node.next = node.next.next
        
        return head