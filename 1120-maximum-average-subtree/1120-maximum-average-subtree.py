# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = 0
        @lru_cache(None)
        def dfs(node):
            if not node:
                return 0, 0
            
            if not node.left and not node.right:
                self.res = max(self.res, node.val)
                return node.val, 1
            
            sum_, tot = dfs(node.left)[0] + dfs(node.right)[0] + node.val,  (dfs(node.left)[1] + dfs(node.right)[1] + 1)
            self.res = max(self.res, sum_/tot)
            return sum_, tot
        
        dfs(root)
        return self.res
        
        