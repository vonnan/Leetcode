class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        if r * c != row * col:
            return mat
        
        lst =[mat[x][y] for x in range(row) for y in range(col)]
        
        res = [[0]*c for _ in range(r)]
        for x in range(r):
            for y in range(c):
                res[x][y] = lst.pop(0)
        
        return res
        
        