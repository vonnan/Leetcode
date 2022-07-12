# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        sets = set([])
        while head:
            if head and head not in sets:
                sets.add(head)
                head = head.next
            else:
                return head
