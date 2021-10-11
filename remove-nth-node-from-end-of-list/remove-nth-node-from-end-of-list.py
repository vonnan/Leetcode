# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size, curr = 0, head
        while curr:
            curr = curr.next
            size += 1
            
        size -= n
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while size:
            curr = curr.next
            size -= 1
            
        curr.next = curr.next.next
        
        return dummy.next