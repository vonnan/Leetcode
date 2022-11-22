class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([0])
        res = 0
        seen = set([0])
        max_ = int(n ** 0.5)
        
        while q:
            m = len(q)
            res += 1
            for _ in range(m):
                x = q.popleft()
                for i in range(1, max_ + 1):
                    new = x + i * i
                    if new == n:
                        return res
                    elif new > n:
                        break
                    elif new not in seen:
                        q.append(new)
                        seen.add(new)
            
                        
                        
        
                