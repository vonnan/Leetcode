# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        res = []
        while head:
            res.append(head.val)
            head = head.next
            
        k %= len(res)
            
        res = res[-k:] + res [:-k]
        dummy = ListNode(-1)
        node = dummy
        
        while res:
            node.next = ListNode(res.pop(0))
            node = node.next
        
        return dummy.next
        