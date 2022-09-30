# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = deque([root])
        while q:
            m = len(q)
            ct = 0
            for _ in range(m):
                node = q.popleft()
                ct += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ct