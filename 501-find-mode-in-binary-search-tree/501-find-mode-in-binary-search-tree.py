# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter([])
        max_ = 0
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            counter[node.val] += 1
            dfs(node.right)
            
        dfs(root)
        max_ = max(counter.values())
        
        return [key for key in counter if counter[key] == max_]
            