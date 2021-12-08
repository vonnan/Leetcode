# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = deque([root])
        while q:
            m = len(q)
            for i in range(m):
                node = q.popleft()
                if node == u:
                    if i == m-1:
                        return 
                    else:
                        return q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                