# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = deque([root])
        seen = set([root.val])
        
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                if k - node.left.val in seen:
                    return True
                seen.add(node.left.val)
            if node.right:
                q.append(node.right)
                if k - node.right.val in seen:
                    return True
                seen.add(node.right.val)
        
        return False