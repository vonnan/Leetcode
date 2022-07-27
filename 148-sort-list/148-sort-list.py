# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        
        while head:
            lst.append(head.val)
            head = head.next
            
        lst.sort(reverse = 1)
        
        dummy = ListNode(-1)
        node = dummy
        while lst:
            node.next = ListNode(lst.pop())
            node = node.next
        
        return dummy.next
            