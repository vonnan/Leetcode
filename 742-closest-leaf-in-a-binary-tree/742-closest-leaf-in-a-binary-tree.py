# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph = defaultdict(list)
        q = deque([root])
        dic = {}
        while q:
            node = q.popleft()
            dic[node.val] = node
            if node.left:
                graph[node.left.val].append(node)
                graph[node.val].append(node.left)
                q.append(node.left)
            if node.right:
                graph[node.right.val].append(node)
                graph[node.val].append(node.right)
                q.append(node.right)
        
        
        if k not in graph:
            return 1
        q = deque([k])
        visited = set([k])
        while q:
            m = len(q)
            for _ in range(m):
                node = dic[q.popleft()]
                if not node.left and not node.right:
                    return node.val
                for u in graph[node.val]:
                    if u.val not in visited:
                        visited.add(u.val)
                        q.append(u.val)
        
                