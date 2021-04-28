# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        memo = {0:1}
        
        def dfs(node, pre_sum, target):
            if not node:
                return 0
            
            count = 0
            
            curr_sum = pre_sum + node.val
            
            if (curr_sum - target) in memo:
                count += memo[curr_sum - target]
            
            if curr_sum in memo:
                memo[curr_sum] += 1
                
            else:
                memo[curr_sum] = 1
                
            count += dfs(node.left, curr_sum, target)
            count += dfs(node.right, curr_sum, target)
            
            memo[curr_sum] -= 1
                
            return count
        
        return dfs(root, 0, targetSum)
            
        
        