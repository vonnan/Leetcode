# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dic = defaultdict(int)
        res = set([])
        
        def dfs(node, path):
            if not node:
                return "#"
            
            path += ",".join([str(node.val), dfs(node.left, path ), dfs(node.right, path)])
            dic[path] += 1
            if dic[path] == 2:
                res.add(node)
            
            return path
        
        dfs(root, "")
        return res
            
        
            
