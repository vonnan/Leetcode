# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longest = 0
        
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            
            left = left + 1 if node.left and node.left.val == node.val else 0
            right = right + 1 if node.right and node.right.val == node.val else 0
            
            self.longest = max(self.longest, left + right)
            
            return max(left, right)
                
        dfs(root)
        
        return self.longest