# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def ifUni(root):
            l, r = True, True
            if root.left:
                if not ifUni(root.left) or root.left.val != root.val:
                    l = False
            
            if root.right:
                if not ifUni(root.right) or root.right.val != root.val:
                    r = False
                    
            res[0] += l and r
            
            return l and r
        
        if not root:
            return 0
        
        ifUni(root)
        return res[0]