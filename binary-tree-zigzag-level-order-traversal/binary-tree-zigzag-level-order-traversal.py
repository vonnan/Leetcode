# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        level = 0
        res = []
        
        while q:
            m = len(q)
            lst = []
            for _ in range(m):
                node = q.popleft()
                lst.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level = 1- level
            if level:
                res.append(lst)
            else:
                res.append(lst[::-1])
        return res
                