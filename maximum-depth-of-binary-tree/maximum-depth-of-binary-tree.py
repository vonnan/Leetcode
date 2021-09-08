# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        level = 0
        
        while queue:
            m = len(queue)
            level += 1
            for _ in range(m):
                node = queue.popleft()
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
                    
        return level
                
            