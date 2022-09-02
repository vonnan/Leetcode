# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = [root.val]
        
        q = deque([root])
        while q:
            lst = []
            m = len(q)
            for _ in range(m):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    lst.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    lst.append(node.right.val)
            if lst:
                res.append(sum(lst)/len(lst))
                
        return res
        