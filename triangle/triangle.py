class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        n = len(A)
        for r in range(1, n):
            A[r][0] += A[r-1][0]
            A[r][r] += A[r-1][r-1]
            for c in range(1, r):
                A[r][c] += min(A[r -1][c], A[r-1][c-1])
        
        return min(A[-1])