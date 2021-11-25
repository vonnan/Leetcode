class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([0])
        visited = set([])
        sqrt_n = int(n ** 0.5)
        step = 0
        
        while q:
            m = len(q)
            step += 1
            for _ in range(m):
                num = q.popleft()
                for val in range(1, sqrt_n + 1):
                    new = num + val * val
                    if new > n:
                        break
                    elif new == n:
                        return step
                    else:
                        if new not in visited:
                            visited.add(new)
                            q.append(new)
        
            
            