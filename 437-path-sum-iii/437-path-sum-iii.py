# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        memo = defaultdict(int)
        memo[0] = 1
        
        def dfs(node, presum):
            if not node:
                return 0
            
            count = 0
            
            curr = presum + node.val
            if curr - targetSum in memo:
                count += memo[curr - targetSum]
                
            memo[curr] += 1
            
            count += dfs(node.left, curr)
            count += dfs(node.right, curr)
            
            memo[curr] -= 1
            return count
        
        return dfs(root, 0)