# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = [root.val]
        
        def dfs(node, isleft, isright):
            if node:
                if (not node.left and not node.right) or isleft:
                    res.append(node.val)
                    
                if node.left and node.right:
                    dfs(node.left, isleft, False)
                    dfs(node.right, False, isright)
                    
                else:
                    dfs(node.left, isleft, isright)
                    dfs(node.right, isleft, isright)
                    
                if (node.left or node.right) and isright:
                    res.append(node.val)
                    
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        
        return res
                    
                    