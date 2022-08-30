# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        level = -1
        q = deque([root])
        while q:
            m = len(q)
            lst = []
            level += 1
            for _ in range(m):
                node = q.popleft()
                lst.append(node.val)
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            
            if level % 2:
                lst.reverse()
            res.append(lst)
        return res
                
            