class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows * cols != r* c:
            return mat
        
        lst = [mat[row][col]  for row in range(rows) for col in range(cols) ]
        print(lst)
        
        res = []
        
        for row in range(r):
            res.append(lst[row* c: (row + 1)* c])
        
        return res
            