# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        
        q = deque([(root, 0, 0)])
        while q:
            node, r, c = q.popleft()
            dic[c].append((r + 1, node.val))
            if node.left:
                q.append((node.left, r + 1, c-1))
            if node.right:
                q.append((node.right, r + 1, c+ 1))
        
        for c in dic:
            dic[c]= [x[1] for x in sorted(dic[c])]
            
        return [dic[c] for c in sorted(dic)]
        
                