# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        dic[0] = [(0, root.val)]
        q = deque([(root,0,  0)])
        while q:
            m = len(q)
            for _ in range(m):
                node, r, c = q.popleft()
                
                if node.left:
                    q.append((node.left, r + 1, c - 1))
                    dic[c-1].append((r + 1, node.left.val))
                if node.right:
                    q.append((node.right, r + 1, c + 1))
                    dic[c+1].append((r + 1, node.right.val))
                    
        for c in dic:
            dic[c].sort()
            dic[c] = [x for _, x in dic[c]]
        
        return [dic[c] for c in sorted(dic)]
                
                
                             
                            
            