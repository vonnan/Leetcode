# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        node = dummy
        
        carry = 0
        while l1 and l2:
            carry, num = divmod(l1.val + l2.val + carry, 10)
            node.next = ListNode(num)
            l1 = l1.next
            l2 = l2.next
            node = node.next
        
        if l1 or l2:
            l = l1 or l2
            while l:
                carry, num = divmod(l.val + carry, 10)
                node.next = ListNode(num)
                l = l.next
                node = node.next
        
        if carry:
            node.next = ListNode(carry)
            node = node.next
            
        return dummy.next