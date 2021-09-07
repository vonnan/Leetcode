# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-1)
        sentinel.next = head
        node = head
        while node and node.next:
            while node.next and node.val == node.next.val:
                if node.next.next:
                    node.next = node.next.next
                else:
                    node.next = None
            node = node.next
        return sentinel.next
        