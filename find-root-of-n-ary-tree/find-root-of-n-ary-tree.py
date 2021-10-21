"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        seen = set([])
        
        for node in tree:
            if node.children:
                for x in node.children:
                    seen.add(x)
                    
        for node in tree:
            if node not in seen:
                return node