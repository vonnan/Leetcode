# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        memo = {0:1}
        
        def dfs(node, presum, target):
            if not node:
                return 0
            count = 0
            
            curr = presum + node.val
            if curr - target in memo:
                count += memo[curr - target]
            
            if curr in memo:
                memo[curr] += 1
            else:
                memo[curr] = 1
            
            count += dfs(node.left, curr, target)
            count += dfs(node.right, curr, target)
            
            memo[curr] -= 1
            return count
        
        return dfs(root, 0, targetSum)
            
            