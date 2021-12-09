"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        res = 0
        
        def dfs(node):
            nonlocal res
            
            max1, max2 = 0, 0
            for child in node.children:
                depth = dfs(child) + 1
                if depth > max1:
                    max1, max2 = depth, max1
                elif depth > max2:
                    max2 = depth
                res = max(res, max1 + max2)
            
            return max1
        
        dfs(root)
        return res
                