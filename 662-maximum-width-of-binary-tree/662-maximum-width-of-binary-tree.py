# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        res = 1
        while q:
            m = len(q)
            for _ in range(m):
                node, pos = q.popleft()
                if node.left:
                    q.append((node.left, 2 * pos))
                if node.right:
                    q.append((node.right, 2 * pos + 1))
                    
            if q:
                res = max(res, q[-1][1] - q[0][1] + 1)
                
        return res