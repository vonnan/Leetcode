class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([0])
        sqrt = int(n ** 0.5)
        visited = set([0])
        
        res = 0
        while q:
            m = len(q)
            res += 1
            for _ in range(m):
                num = q.popleft()
                for i in range(1, sqrt + 1):
                    new = i * i + num
                    if new > n:
                        break
                    if new == n:
                        return res
                    else:
                        if new not in visited:
                            q.append(new)
                            visited.add(new)
            
                            
                            