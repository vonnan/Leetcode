# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        dfs = [root]
        
        while root and dfs:
            root = dfs.pop()
            if root.right:
                dfs.append(root.right)
            
            if root.left:
                dfs.append(root.left)
                root.right = root.left
                root.left = None
            else:
                if dfs:
                    root.right = dfs[-1]
                    root.left = None
            