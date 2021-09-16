# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(x,y):
            if not (x and y):
                return x is y
            
            return (x.val == y.val and isSame(x.left, y.left) and isSame(x.right, y.right))
            
        if not root:
            return False
        
        if isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
                