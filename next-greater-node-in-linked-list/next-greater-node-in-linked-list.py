# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        res = []
        
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
            
            
        n = len(lst)
        
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= lst[i]:
                stack.pop()
                
            if stack:
                res.append(stack[-1])
            else:
                res.append(0)
                
            stack.append(lst[i])
        
        return res[::-1]
        