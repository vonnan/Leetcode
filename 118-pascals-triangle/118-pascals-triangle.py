class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res = [[1]* i for i in range(1, n+1)]
        
        if n <= 2:
            return res
        
        for r in range(1, n-1):
            for c in range(r):
                res[r + 1][c + 1] = res[r][c] + res[r][c+1]
        
        return res
