# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_, max_ = min(p.val, q.val), max(p.val, q.val)
        ans = root
        
        while not min_ <= ans.val <= max_:
            if ans.val < min_:
                ans = ans.right
            
            elif ans.val > max_:
                ans = ans.left
                
        return ans