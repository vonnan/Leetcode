# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_ = abs(root.val - target)
        res = root.val
        
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == target:
                return node.val
            elif node.val > target:
                if node.left:
                    q.append(node.left)
                
                if node.val - target < min_:
                    min_ = node.val - target
                    res = node.val
            else:
                if node.right:
                    q.append(node.right)
                
                if  target - node.val < min_:
                    min_ = target - node.val
                    res = node.val
        return res
                    
                
        