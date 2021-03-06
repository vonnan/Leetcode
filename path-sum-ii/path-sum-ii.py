# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        if not root.right and not root.left:
            if root.val == targetSum:
                return [[root.val]]
            else:
                return []
            
        left = self.pathSum(root.left, targetSum - root.val)
        right = self.pathSum(root.right, targetSum - root.val)
        
        left = [[root.val] + l for l in left]
        right = [[root.val] + r for r in right]
        
        return left + right
                
                
                