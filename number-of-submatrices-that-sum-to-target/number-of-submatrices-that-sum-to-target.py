class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row, col = len(matrix), len(matrix[0])
        
        for r in range(row):
            for c in range(1, col):
                matrix[r][c] += matrix[r][c-1]
                
        res = 0
        
        for c1 in range(col):
            for c2 in range(c1, col):
                arr = [matrix[r][c2] - (matrix[r][c1 - 1] if c1 >0 else 0) for r in range(row)]
                
                curr = 0
                presum = defaultdict(int)
                for a in arr:
                    presum[curr] += 1
                    curr += a
                    if curr- target in presum:
                        res += presum[curr - target]
                        
        return res
                    