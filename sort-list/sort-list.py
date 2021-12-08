# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        node = head
        while node:
            lst.append(node.val)
            node = node.next
            
        lst.sort(reverse = 1)
        
        dummy = node = ListNode(-1)
        while lst:
            nxt = ListNode(lst.pop())
            node.next = nxt
            node = node.next
        return dummy.next