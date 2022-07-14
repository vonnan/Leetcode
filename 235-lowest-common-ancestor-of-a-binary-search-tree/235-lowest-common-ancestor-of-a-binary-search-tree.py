# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_, max_ = min(p.val, q.val), max(p.val, q.val)
        while root:
            val = root.val
            if min_ <= val <= max_:
                return root
            
            elif max_ < val:
                return self.lowestCommonAncestor(root.left, p, q )
            
            elif min_ > val:
                return self.lowestCommonAncestor(root.right, p, q )
            