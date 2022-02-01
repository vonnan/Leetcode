class Solution:
    def knightProbability(self, n: int, k: int, row: int, col: int) -> float:
        path = [(1,2), (2,1), (-1,2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
        @lru_cache(None)
        def dfs(r,c, k):
            if not (0 <= r < n and 0 <= c < n):
                return 0
            if k == 0:
                return 1
            
            return sum(dfs(r+dr, c+dc, k-1) for dr,dc in path)/8
        
        return dfs(row, col, k)
        