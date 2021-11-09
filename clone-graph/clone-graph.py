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
        
        q = deque([node])
        seen = {}
        seen[node] = Node(node.val, [])
        
        while q:
            x = q.popleft()
            for nei in x.neighbors:
                if nei not in seen:
                    seen[nei] = Node(nei.val, [])
                    q.append(nei)
                seen[x].neighbors.append(seen[nei])
        return seen[node]
            