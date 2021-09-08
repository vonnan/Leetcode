# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(rt1, rt2):
            if (not rt1) or (not rt2):
                return (not rt1) and (not rt2) 
            
            if rt1.val != rt2.val:
                return False
            
            else:
                return helper(rt1.left, rt2.right) and helper(rt1.right, rt2.left)
            
        return helper(root, root)