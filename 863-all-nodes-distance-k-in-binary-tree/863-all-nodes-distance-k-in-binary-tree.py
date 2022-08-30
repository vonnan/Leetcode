# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        
        nei = defaultdict(set)
        
        def dfs(parent, child):
            if parent and child:
                nei[parent.val].add(child.val)
                nei[child.val].add(parent.val)
            if child:
                dfs(child, child.left)
                dfs(child, child.right)
                
        dfs(None, root)
        
        visited = set([target.val])
        q = deque([target.val])
        res = [target.val]
        
        while k:
            k -= 1
            m = len(q)
            res = []
            for _ in range(m):
                node = q.popleft()
                
                for nbr in nei[node]:
                    if nbr not in visited:
                        visited.add(nbr)
                        q.append(nbr)
                        res.append(nbr)
            
        return res
                    
                