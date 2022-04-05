# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.val = 0
        def helper(node):
            if not node:
                return
            
            helper(node.right)
            self.val +=  node.val
            node.val = self.val
            helper(node.left)
        
        helper(root)
        return root
            