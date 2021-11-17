class Solution:
    def getRow(self, n: int) -> List[int]:
        res = [[1] * (i + 1) for i in range(n + 1)]
        
        if n <= 1:
            return res[-1]
        
        for i in range(2, n + 1):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
                
        return res[-1]