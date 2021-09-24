"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack, curr = [], head
        
        while stack or curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                child = curr.child
                child.prev = curr
                curr.child = None
                curr.next = child
                
            elif not curr.next and stack:
                curr.next = stack.pop()
                curr.next.prev = curr
            
            curr = curr.next
        
        return head
                