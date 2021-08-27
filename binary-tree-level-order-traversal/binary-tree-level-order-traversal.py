# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque([root])
        res = []
        if not root:
            return []
        while queue:
            curr, m = [], len(queue)
            for _ in range(m):
                node = queue.popleft()
                if node:
                    curr.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            res.append(curr)
        return res
        