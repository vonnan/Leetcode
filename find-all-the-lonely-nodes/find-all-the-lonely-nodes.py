# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        
        while q:
            node = q.popleft()
            if node.left and node.right:
                q.append(node.left)
                q.append(node.right)
            elif not node.left and not node.right:
                continue
            else:
                nxt = node.left or node.right
                res.append(nxt.val)
                q.append(nxt)
        return res