# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        dic = defaultdict(list)
        q = deque([(0,root)])
        
        while q:
            col, node = q.popleft()
            dic[col].append(node.val)
            if node.left:
                
                q.append((col -1, node.left))
            if node.right:
                
                q.append((col + 1, node.right))
        
        return [val for key, val in sorted(dic.items())]