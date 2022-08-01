# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []
        if not root:
            return res
        
        while q:
            lst = []
            m = len(q)
            for _ in range(m):
                node = q.popleft()
                lst.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(lst)
        return res[::-1]