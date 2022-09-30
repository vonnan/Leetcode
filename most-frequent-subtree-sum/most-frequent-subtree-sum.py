# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter()
        
        def dfs(node):
            if not node:
                return 0
            
            val = node.val + dfs(node.left) + dfs(node.right)
            counter[val] += 1
            return val
        
        dfs(root)
        max_ = max(counter.values())
        return [ key for key, val in counter.items() if val == max_]