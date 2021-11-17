# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def find_middle(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse(node):
            prev, curr = None, node
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev
        
        rev = reverse(find_middle(head))
        first, second = head, rev
        
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        
        return head
           
            
            
        
            