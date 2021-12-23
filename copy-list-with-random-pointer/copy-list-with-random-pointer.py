"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        memo = {}
        
        def deepcopy(node):
            if not node:
                return
            
            if node in memo:
                return memo[node]
            
            memo[node] = new = Node(node.val)
            
            new.next = deepcopy(node.next)
            new.random = deepcopy(node.random)
            
            return new
        
        return deepcopy(head)
        