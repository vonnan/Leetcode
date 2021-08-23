# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = deque([root])
        seen = set()
        while queue:
            u = queue.popleft()
            if k - u.val in seen:
                return True
            else:
                seen.add(u.val)
            
            if u.left:
                queue.append(u.left)
            if u.right:
                queue.append(u.right)
                
        return False