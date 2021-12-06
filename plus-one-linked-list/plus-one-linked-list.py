# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def dfs(node):
            if not node:
                return 1
            
            carry = dfs(node.next)
            carry, node.val = divmod(node.val + carry, 10)
            return carry
        
        carry = dfs(head)
        if carry:
            newhead = ListNode(carry)
            newhead.next = head
            return newhead
        else:
            return head
            