"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        seen = {}
        seen[node] = Node(node.val, [])
        
        q = deque([node])
        while q:
            m = len(q)
            for _ in range(m):
                nd = q.popleft()
                for nei in nd.neighbors:
                    if nei not in seen:
                        seen[nei] = Node(nei.val, [])
                        q.append(nei)
                    seen[nd].neighbors.append(seen[nei])
        
        return seen[node]