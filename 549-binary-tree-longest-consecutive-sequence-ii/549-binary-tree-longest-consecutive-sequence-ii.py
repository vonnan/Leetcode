# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node):
            if not node:
                return 0, 0
            
            up, down = 1, 1
            
            l_up, l_down = dfs(node.left)
            r_up, r_down = dfs(node.right)
            
            if node.left:
                if node.left.val == node.val + 1:
                    up = max(up, l_up + 1)
                elif node.left.val == node.val - 1:
                    down = max(down, l_down + 1)
            
            if node.right:
                if node.right.val == node.val + 1:
                    up = max(up, r_up + 1)
                elif node.right.val == node.val - 1:
                    down = max(down, r_down + 1)
                    
            self.res = max(self.res, up + down - 1)
            
            return up, down
        
        dfs(root)
        return self.res