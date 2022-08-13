# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        tot = 0
        
        q = deque([root])
        while q:
            m = len(q)
            for _ in range(m):
                node = q.popleft()
                tot += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        if tot % 2:
            return False
        
        @lru_cache(None)
        def dfs(node):
            if not node:
                return 0
            
            return node.val + dfs(node.left) + dfs(node.right)
        
        target = tot // 2
        q = deque([])
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
        
        while q:
            node = q.popleft()
            val = dfs(node)
            if val == target:
                return True
              
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return False
            
        
                