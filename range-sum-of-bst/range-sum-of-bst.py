# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect_left
from bisect import bisect

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        lst = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
            
        dfs(root)
        
        left = bisect_left(lst, low)
        right = bisect(lst, high)
        
        return sum(lst[left: right])