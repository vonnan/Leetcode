"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
       
        if not root:
            return None
        
        dummy = Node(-1)
        prev = dummy
        
        def inorder(root):
            nonlocal prev
            if not root:
                return
            
            inorder(root.left)
            
            prev.right, root.left, prev = root, prev, root
            
            inorder(root.right)
            
        inorder(root)
        dummy.right.left, prev.right = prev, dummy.right
        
        return dummy.right
    
       