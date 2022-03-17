# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        
        res = TreeNode(preorder[0])
        
        idx = bisect(preorder, preorder[0])
        res.left = self.bstFromPreorder(preorder[1:idx])
        res.right = self.bstFromPreorder(preorder[idx:])
        return res