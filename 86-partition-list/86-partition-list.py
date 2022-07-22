# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(-1), ListNode(-1)
        node_l, node_r = left, right
        while head:
            if head.val < x:
                node_l.next = ListNode(head.val)
                node_l = node_l.next
            else:
                node_r.next = ListNode(head.val)
                node_r = node_r.next
            
            head = head.next
        node_l.next = right.next
        return left.next