class Solution:
    def calculateMinimumHP(self, A: List[List[int]]) -> int:
        row, col = len(A), len(A[0])
        path = [(-1,0), (0, -1)]
        q = deque([(row-1, col-1)])
        dp = [[inf] * col for _ in range(row)]
       
        dp[-1][-1] = max(-A[-1][-1], 0) +1

        while q:
            r,c= q.popleft()
            for dr, dc in path:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    if dp[r][c] - A[nr][c] < dp[nr][nc]:
                        dp[nr][nc] = max(dp[r][c] - A[nr][nc],1)
                        q.append((nr, nc))
            
        
        return dp[0][0]     