# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = [head]
        while stack[-1].next:
            stack.append(stack[-1].next)
        return stack[len(stack)//2]
            
 
        