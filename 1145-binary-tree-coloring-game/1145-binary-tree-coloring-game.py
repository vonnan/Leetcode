# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        ct = [0, 0]
        
        def count(node):
            if not node:
                return 0
            
            left, right = count(node.left), count(node.right)
            
            if node.val == x:
                ct[0], ct[1] = left, right
            
            return left + right + 1
        
        count(root)
        print(ct)
        return n/2 < max(max(ct), n - sum(ct) - 1)