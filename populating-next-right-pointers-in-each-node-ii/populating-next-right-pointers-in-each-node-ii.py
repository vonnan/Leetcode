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
        dic = {}
        def dfs(node, pt):
            if not node:
                return
            
            if pt in dic:
                dic[pt].next = node
            
            dic[pt] = node
            node.next = None
            
            dfs(node.left, pt + 1)
            dfs(node.right, pt + 1)
            
        dfs(root, 0)
        return root
                
                