# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, root.val, root.val)])
        
        res = 0
        while q:
            node, min_, max_ = q.popleft()
            res = max(res, max_ - min_)
            if node.left:
                if node.left.val < min_:
                    q.append((node.left, node.left.val, max_))
                elif node.left.val > max_:
                    q.append((node.left, min_, node.left.val))
                else:
                    q.append((node.left, min_, max_))
            if node.right:
                if node.right.val < min_:
                    q.append((node.right, node.right.val, max_))
                elif node.right.val > max_:
                    q.append((node.right, min_, node.right.val))
                else:
                    q.append((node.right, min_, max_))
        return res