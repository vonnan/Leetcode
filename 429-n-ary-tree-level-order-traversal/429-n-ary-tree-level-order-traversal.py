"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        
        q = deque([root])
        while q:
            m = len(q)
            lst = []
            for _ in range(m):
                node = q.popleft()
                lst.append(node.val)
                for v in node.children:
                    q.append(v)
            res.append(lst)
        return res
                