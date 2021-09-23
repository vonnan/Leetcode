# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def getorder(node):
            if not node:
                return
            
            if node.left:
                getorder(node.left)
                
            res.append(node.val)
            
            if node.right:
                getorder(node.right)
                
        res = []
        getorder(root)
        
        return res == sorted(res) and len(res) == len(set(res))
