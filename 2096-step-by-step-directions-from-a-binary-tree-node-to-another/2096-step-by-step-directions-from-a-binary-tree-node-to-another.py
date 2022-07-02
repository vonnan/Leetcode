# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getDirections(self, root: Optional[TreeNode], A: int, B: int) -> str:
        
        dic = defaultdict(dict)
        q = deque([root])
        
        while q:
            m = len(q)
            for _ in range(m):
                node = q.popleft()
                if node.left:
                    dic[node.left.val][node.val] = "U"
                    dic[node.val][node.left.val] = "L"
                    q.append(node.left)
                if node.right:
                    dic[node.right.val][node.val] = "U"
                    dic[node.val][node.right.val] = "R"
                    q.append(node.right)
        
        q = deque([(A, "")])
        visited = set([A])
        while q:
            m = len(q)
            for _ in range(m):
                u, path = q.popleft()
                for v in dic[u]:
                    if v not in visited:
                        visited.add(v)
                        new = path + dic[u][v]
                        if v == B:
                            return new
                        q.append((v, new))
                        
                
                
