# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = []
        
        while head:
            lst.append(head.val)
            head = head.next
        
        lst[left -1:right] = lst[left - 1:right][::-1]
        #print(lst, lst[left +1:right],lst[left + 1:right][::-1] )
        dummy = ListNode(-1)
        node = dummy
        while lst:
            node.next = ListNode(lst.pop(0))
            node = node.next
        return dummy.next
            