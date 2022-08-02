# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            res.append((abs(node.val-target), node.val))
            dfs(node.right)
        
        dfs(root)
        res.sort()
        
        return [val for _, val in res[:k]]
        
        