class Solution:
    def maxPoints(self, A: List[List[int]]) -> int:
        row, col = len(A), len(A[0])
        
        for r in range(row -1):
            for c in range(col-2, -1, -1):
                A[r][c] = max(A[r][c], A[r][c+1] - 1)
                
            for c in range(col):
                A[r][c] = max(A[r][c], A[r][c-1] -1 if c else 0)
                
                A[r + 1][c] += A[r][c]
        
        return max(A[-1])