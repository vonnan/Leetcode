"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        q = deque([root])
        level = 0
        while q:
            m = len(q)
            level += 1
            for _ in range(m):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
        return level