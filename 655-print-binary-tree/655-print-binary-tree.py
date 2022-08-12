# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        q = deque([root])
        level = 0
        while q:
            m = len(q)
            for _ in range(m):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        row, col = level, 2** level - 1
        
        dp = [[""] * col for _ in range(row)]
        r = 0
        q = deque([(root,r, col//2)])
        while q:
            m = len(q)
            
            for _ in range(m):
                node, r, c = q.popleft()
                
                dp[r][c] = str(node.val)
                
                if node.left:
                    q.append((node.left, r + 1, c - 2**(level - r - 2)))
                if node.right:
                    q.append((node.right, r + 1, c + 2**(level - r - 2)))
        
        return dp
                    
        