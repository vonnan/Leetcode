# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        
        depth -= 1
        q = deque([(root, 1)])
        
        while q:
            m = len(q)
            for _ in range(m):
                node, d = q.popleft()
                if node:
                    if d == depth:
                    
                        node.left, node.right = TreeNode(val, node.left, None), TreeNode(val, None, node.right)
                    q.extend([(node.left, d + 1), (node.right, d+ 1)])
        return root
