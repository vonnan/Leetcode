class Solution:
    def maxPoints(self, A: List[List[int]]) -> int:
        rows, cols = len(A), len(A[0])
        for r in range(rows - 1):
            for c in range(cols-2, -1, -1):
                A[r][c] = max(A[r][c], A[r][c+1] -1)
            for c in range(cols):
                A[r][c] = max(A[r][c], A[r][c-1] -1 if c else 0)
                A[r+1][c] += A[r][c]
                
        return max(A[-1])