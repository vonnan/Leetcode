# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size, curr = 0, head
        
        while curr:
            curr = curr.next
            size += 1
            
        if size == 1:
            return head
            
        mid, curr = (size + 1)//2, head
        
        while curr:
            curr = curr.next
            size -= 1
            
            if size == mid:
                return curr
            
            
        
        