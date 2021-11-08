# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        nei_level = defaultdict(set)
        def graph(parent, child):
            if parent and child:
                nei_level[parent.val].add(child.val)
                nei_level[child.val].add(parent.val)
            if child:
                graph(child, child.left)
                graph(child, child.right)
            
        graph(None, root)
        
        q = deque([target.val])
        seen = set([target.val])
        print(nei_level, q, seen)
        while K:
            m = len(q)
            res = []
            for _ in range(m):
                val = q.popleft()
                for nei in nei_level[val]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
                        
            K -= 1
            
        return list(q)
            
        
            
                
            
            
       
            