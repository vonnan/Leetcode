# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        ans = dummy
        pos = 1
        while left != 1:
            left -= 1
            pos += 1
            dummy = dummy.next
        first = dummy
        second = dummy.next
        dummy = dummy.next
        rev = None
        while pos != right +1:
            rev, rev.next, dummy = dummy, rev, dummy.next
            pos += 1
        first.next, second.next = rev, dummy
        return ans.next