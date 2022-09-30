# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag = 1
        q = deque([root])
        res = []
        if not root:
            return res
        
        while q:
            m = len(q)
            lst = []
            
            flag = 1 - flag
            for _ in range(m):
                node = q.popleft()
                lst.append(node.val)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                    
            if flag:
                res.append(lst[::-1])
            else:
                res.append(lst)
        
        return res