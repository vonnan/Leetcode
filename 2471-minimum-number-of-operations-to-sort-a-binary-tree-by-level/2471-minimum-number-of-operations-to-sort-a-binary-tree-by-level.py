# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        def cntSwaps(a):
            m = {n: j for j, n in enumerate(sorted(a))}
            cnt = i = 0
            while i < len(a):
                j = m[a[i]]
                if i != j:
                    a[i], a[j] = a[j], a[i]
                    cnt += 1
                else:
                    i += 1
            return cnt
        
        q = deque([root])
        res = 0
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res += cntSwaps([n.val for n in q])
        return res                
                    