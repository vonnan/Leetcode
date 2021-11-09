class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[1] * n for _ in range(n)]
        
        rs, cs, re, ce = 0, 0, n-1, n-1
        ct = 1
        
        while rs <= re and cs <= ce:
            for c in range(cs, ce + 1):
                res[rs][c] = ct
                ct += 1
            for r in range(rs+1, re):
                res[r][ce] = ct
                ct += 1
            for c in range(ce, cs, -1):
                res[re][c] = ct
                ct += 1
            for r in range(re, rs, -1):
                res[r][cs] = ct
                ct += 1
                
            rs += 1
            cs += 1
            re -= 1
            ce -= 1
        
        return res