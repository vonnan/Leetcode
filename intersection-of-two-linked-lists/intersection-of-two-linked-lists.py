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
        seen.add(headB)
        while headA or headB:
            if headA:
                headA = headA.next
                if headA in seen:
                    return headA
                seen.add(headA)
            if headB:
                headB = headB.next
                if headB in seen:
                    return headB
                seen.add(headB)
                
        
            