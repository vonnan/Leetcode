# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        res = 1
        while q:
            m = len(q)
            for _ in range(m):
                node, val = q.popleft()
                if node.left:
                    if node.left.val == node.val + 1:
                        q.append((node.left, val + 1))
                        res = max(res, val + 1)
                    else:
                        q.append((node.left, 1))
                
                if node.right:
                    if node.right.val == node.val + 1:
                        q.append((node.right, val + 1))
                        res = max(res, val + 1)
                    else:
                        q.append((node.right, 1))
        
        return res
                    