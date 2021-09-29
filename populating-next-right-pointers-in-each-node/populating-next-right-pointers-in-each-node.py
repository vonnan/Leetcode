"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        q = deque([root])
        
        while q:
            m = len(q)
            for i in range(m):
                node = q.popleft()
                if i < m-1:
                    node.next = q[0]
                
                if node.left and node.right:
                    q.append(node.left)
                    q.append(node.right)
        
        return root
                
    
    