# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0, 0)])
        res = 1
        while q:
            m = len(q)
            for _ in range(m):
                node, depth, pos = q.popleft()
                if node.left:
                    q.append((node.left, depth + 1, pos*2))
                if node.right:
                    q.append((node.right, depth + 1, pos * 2 + 1))
            if q:
                res = max(res, q[-1][-1] - q[0][-1] + 1)
        return res
            