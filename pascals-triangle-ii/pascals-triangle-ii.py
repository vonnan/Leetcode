class Solution:
    def getRow(self, r: int) -> List[int]:
        res = [[1] * (i + 1) for i in range(r + 1)]
        if r <= 1:
            return res[-1]
        
        for i in range(1, r + 1):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        
        return res[-1]