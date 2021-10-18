# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        sets = set([x, y])
        
        q = deque([root])
        flag = False
        while q:
            m = len(q)
            res = []
            for _ in range(m):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    if node.left.val in sets:
                        if node.right and node.right.val in sets:
                            return False
                        else:
                            res.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    if node.right.val in sets:
                        res.append(node.right.val)
            if res and len(res) != 2:
                return False
            elif len(res) == 2:
                return True
            
                    
                    
                        