class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        row, col = len(mat), len(mat[0])
        dp = [[0] * ( col + 1) for _ in range(row + 1)]
        if min(min(row) for row in mat) > threshold:
            return 0
        
        for r in range(row):
            for c in range(col):
                dp[r+1][c+1] = mat[r][c] + dp[r+1][c] + dp[r][c+1] - dp[r][c]
        
        def ifValid(size):
            for r in range(row - size + 1):
                for c in range(col - size + 1):
                    tot = dp[r + size][c+size] + dp[r][c] - dp[r+size][c] - dp[r][c+size]
                    if tot <= threshold:
                        return True
            
            return False
        
        left, right= 0, min(row, col) 
        while left < right:
            mid = (left + right + 1)//2
            if ifValid(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
            
            
        