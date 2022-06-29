# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        sorted_ = sorted(res)
        dic = {}
        for a, b in zip(res, sorted_):
            if a != b:
                dic[a] = b
                dic[b] = a
                break
        
        q = deque([root])
        ct = 2
        while q:
            node = q.popleft()
            if node.val in dic:
                node.val = dic[node.val]
                ct -= 1
                if ct == 0:
                    break
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
            
                
            
        
        
        