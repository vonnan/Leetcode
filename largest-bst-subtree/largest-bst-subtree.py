# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return float("inf"), float("-inf"), 0
        
            left_min, left_max, left_size = dfs(node.left)
            right_min, right_max, right_size = dfs(node.right)
            
            if left_max < node.val < right_min:
                return min(left_min, node.val), max(right_max, node.val), left_size + right_size +1
            
            else:
                return float("-inf"), float("inf"), max(left_size, right_size)
            
        return dfs(root)[-1]
        