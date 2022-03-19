# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        def helper(node, is_root):
            if not node:
                return
            
            to_remove = node.val in to_delete
            
            if is_root and not to_remove:
                res.append(node)
            
            node.left = helper(node.left, to_remove)
            node.right = helper(node.right, to_remove)
            
            return None if to_remove else node
        
        helper(root, True)
        return res
            