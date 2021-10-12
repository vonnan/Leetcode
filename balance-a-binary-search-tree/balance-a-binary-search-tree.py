# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
            
        dfs(root)
        
        def bst(node):
            if not node:
                return
            mid = len(node)//2
            res = TreeNode(node[mid])
            res.left = bst(node[:mid])
            res.right = bst(node[mid+1:])
            return res
        
        return bst(inorder)