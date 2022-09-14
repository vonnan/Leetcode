# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
       
        def dfs(node, sets):
            if not node:
                return
            
            if not node.left and not node.right:
                if len(sets) <= 1:
                    self.res += 1
            
            if node.left:
                if node.left.val in sets:
                    dfs(node.left, sets - set([node.left.val]))
                else:
                    dfs(node.left, sets| set([node.left.val]))
                    
            if node.right:
                if node.right.val in sets:
                    dfs(node.right, sets - set([node.right.val]))
                else:
                    dfs(node.right, sets | set([node.right.val]))
            
        dfs(root, set([root.val]))
        return self.res
                
            
            