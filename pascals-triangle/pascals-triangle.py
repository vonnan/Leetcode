class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * i for i in range(1, numRows + 1)]
        if numRows <= 2:
            return res
        
        for r in range(2, numRows):
            for c in range(1, r):
                res[r][c] = res[r-1][c-1] + res[r-1][c]
        
        return res