# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        q = deque([root])
        while root and q:
            root = q.pop()
            
            if root.right:
                q.append(root.right)
                
            if root.left:
                q.append(root.left)
                root.right = root.left
                root.left  = None
            else:
                if q:
                    root.right = q[-1]
                    root.left = None