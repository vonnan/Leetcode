# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.dfs(root)[1]
        
    def dfs(self, node):
        if not node:
            return (0, 0)
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        return (left[1] + right[1], max(left[1] + right[1], left[0] + right[0] + node.val))
        
        
        
            