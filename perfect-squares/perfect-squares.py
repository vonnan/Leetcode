class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([0])
        visited = set([])
        
        sqrt = int(n ** 0.5) + 1
        step = 0
        
        while q:
            m = len(q)
            step += 1
            for _ in range(m):
                x = q.popleft()
                for i in range(1, sqrt):
                    new = i * i + x
                    if new in visited:
                        continue
                    if new > n:
                        break
                    if new < n:
                        q.append(new)
                        visited.add(new)
                    elif new == n:
                        return step
            
                    
                