class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        row, col = len(mat), len(mat[0])
        dp = [[0]* (col + 1) for _ in range(row + 1)]
        
        for r in range(row):
            for c in range(col):
                dp[r+1][c+1] = mat[r][c] + dp[r+1][c] + dp[r][c + 1] - dp[r][c]
        
        def isvalid(size):
            for r in range(row - size + 1):
                for c in range(col - size + 1):
                    if dp[r][c] - dp[r+size][c] - dp[r][c + size] + dp[r + size][c + size] <= threshold:
                        return True
            return False
        
        lo, hi = 0, min(row, col)
        while lo < hi:
            mid = (lo + hi + 1)//2
            if isvalid(mid):
                lo = mid
            else:
                hi = mid -1
        return hi
            