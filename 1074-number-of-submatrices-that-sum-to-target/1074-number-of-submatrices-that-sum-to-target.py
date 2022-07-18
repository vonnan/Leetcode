class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row, col = len(matrix), len(matrix[0])
        for r in range(row):
            matrix[r] = [0] + matrix[r]
            for c in range(col):
                matrix[r][c + 1] += matrix[r][c]
        
        matrix = [[0] * (col + 1)] + matrix
        res, mod = 0, 10**9 + 7
        
        for c1 in range(col):
            for c2 in range(c1, col):
                prefix =[0]
                dic = defaultdict(int)
                dic[0] = 1
                for r in range(row):
                    x = matrix[r+1][c2+1] - matrix[r+1][c1]
                    x += prefix[-1]
                    if x- target in dic:
                        res += dic[x- target]
                        
                    prefix.append(x)
                    dic[x] += 1
            
        return res
                
                
                
        
