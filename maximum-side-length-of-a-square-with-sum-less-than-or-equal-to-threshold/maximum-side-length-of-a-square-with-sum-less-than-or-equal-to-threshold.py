class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        row, col = len(mat), len(mat[0])
        presum = [[0] * (col +1) for _ in range(row + 1)]
        
        for r in range(row):
            for c in range(col):
                presum[r+1][c+1] = mat[r][c] + presum[r+1][c] + presum[r][c+1] - presum[r][c]
                
        def isValid(size):
            for r in range(row +1 -size):
                for c in range(col + 1 - size):
                    if presum[r+size][c+size] + presum[r][c] - presum[r+size][c] - presum[r][c+size] <= threshold:
                        return True
            return False
        
        lo, hi = 0, min(row, col)
        while lo < hi:
            mid = (lo + hi + 1)//2
            if isValid(mid):
                lo = mid
            else:
                hi = mid -1
        return lo
        