# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, root.val)])
        res = 1
        
        while q:
            m = len(q)
            for _ in range(m):
                node, max_ = q.popleft()
                if node.left:
                    if node.left.val >= max_:
                        res += 1
                        q.append((node.left, node.left.val))
                    else:
                        q.append((node.left, max_))
                if node.right:
                    if node.right.val >= max_:
                        res += 1
                        q.append((node.right, node.right.val))
                    else:
                        q.append((node.right, max_))
        return res
                
            
            