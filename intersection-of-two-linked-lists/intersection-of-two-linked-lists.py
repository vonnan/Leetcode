# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set([headA])
        if headB in seen:
            return headB
        
        while headA:
            headA = headA.next
            seen.add(headA)
        
        while headB:
            if headB in seen:
                return headB
            headB = headB.next
        
        