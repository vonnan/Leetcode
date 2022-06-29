# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        
        q = deque([(root, [root.val])])
        
        while q:
            node, path = q.popleft()
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                q.append((node.left, path + [node.left.val]))
            if node.right:
                q.append((node.right, path + [node.right.val]))
        
        def convert(path):
            return  int("".join([str(x) for x in path]))
        
        return sum(convert(path) for path in res)
        
        
        
        
        
        