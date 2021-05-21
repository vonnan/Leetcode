from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row, col = len(matrix), len(matrix[0])
        
        for r in range(row):
            for c in range(1,col):
                matrix[r][c] += matrix[r][c-1]
        
        res = 0
        
        for c1 in range(col):
            for c2 in range(c1, col):
                presum = defaultdict(int)
                presum[0] = 1
                curr = 0
                for r in range(row):
                    if c1==0:
                        curr += matrix[r][c2]
                    else:
                        curr += matrix[r][c2] - matrix[r][c1-1]
                    res += presum[curr - target]
                    presum[curr] += 1
        return res
                    
                    
        