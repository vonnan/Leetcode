class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[1] * n for _ in range(n)]
        
        rs, cs, re, ce = 0, 0, n-1, n-1
        ct = 1
        
        while cs <= ce and rs <= re:
            for c in range(cs, ce + 1):
                matrix[rs][c] = ct
                ct += 1
            for r in range(rs + 1, re):
                matrix[r][ce] = ct
                ct += 1
            for c in range(ce, cs, -1):
                matrix[re][c] = ct
                ct += 1
            for r in range(re, rs, -1):
                matrix[r][cs] = ct 
                ct += 1
            
            rs += 1
            cs += 1
            re -= 1
            ce -= 1
            
        return matrix