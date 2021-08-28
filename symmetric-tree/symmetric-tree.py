# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(root1, root2):
            if not root1 or not root2:
                return not root1 and not root2
            
            return root1.val == root2.val and helper(root1.right, root2.left) and helper(root1.left, root2.right)
        
        return helper(root, root)
        