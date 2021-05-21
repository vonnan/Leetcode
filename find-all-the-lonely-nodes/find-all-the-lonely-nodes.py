# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return []
        
        def dfs(node):
            nonlocal res
            
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and (not right):
                res.append(node.left.val)
                
            elif right and (not left):
                res.append(node.right.val)
                
            return True
                
         
        dfs(root)
        
        return res
            
        
            
        