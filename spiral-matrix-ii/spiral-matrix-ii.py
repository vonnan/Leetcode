class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix =[[0] * n for _ in range(n)]
        
        rs,re, cs, ce= 0, n-1, 0, n-1
        ct = 1
        while rs<= re and cs <= ce:
            for c in range(cs, ce + 1):
                matrix[rs][c] = ct
                ct += 1
            for r in range(rs + 1, re + 1):
                matrix[r][ce] = ct
                ct += 1
            for c in range(ce-1, cs-1, -1):
                matrix[re][c] = ct
                ct += 1
            for r in range(re-1, rs, -1):
                matrix[r][cs] = ct
                ct += 1
            rs += 1
            re -= 1
            cs += 1
            ce -= 1
        
        return matrix