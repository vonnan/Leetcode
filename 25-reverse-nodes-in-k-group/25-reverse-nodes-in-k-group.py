# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        tail = head
        for _ in range(k):
            if not tail:
                return head
            tail = tail.next
            
        tail = self.reverseKGroup(tail, k)
        
        for _ in range(k):
            head.next, tail, head = tail, head, head.next
        
        return tail