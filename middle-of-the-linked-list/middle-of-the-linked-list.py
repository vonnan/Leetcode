# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        node = head
        while node:
            node = node.next
            size += 1
        
        if size == 1:
            return head
        
        mid = (size + 1) //2
        
        node = head

        while node:
            node = node.next
            size -= 1
            
            if size == mid:
                return node