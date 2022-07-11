# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        q = deque([root])
        res = [root.val]
        while q:
            m = len(q)
            lst = inf
            for i in range(m):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    lst = node.left.val
                if node.right:
                    q.append(node.right)
                    lst = node.right.val
            if lst != inf:
                res.append(lst)
        return res
                
       