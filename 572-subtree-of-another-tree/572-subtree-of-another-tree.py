# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(node1, node2):
            if not (node1 and node2):
                return node1 is node2
            
            return node1.val == node2.val and same(node1.left, node2.left) and same(node1.right, node2.right)
        
        def dfs(root):
            if same(root, subRoot):
                return True
            
            if not root:
                return False
            
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)