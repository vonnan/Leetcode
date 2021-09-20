class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]* i for i in range(1, numRows + 1)]
        if numRows <= 2:
            return res
        
        for i in range(3, numRows + 1):
            for j in range(1, i-1):
                res[i-1][j] = res[i-2][j-1] + res[i-2][j]
        
        return res