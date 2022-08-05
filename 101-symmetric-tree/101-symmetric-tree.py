# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            else:
                if node1.val != node2.val:
                    return False
                return helper(node1.right, node2.left) and helper(node1.left, node2.right)
        
        return helper(root.left, root.right)