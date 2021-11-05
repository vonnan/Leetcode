class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat), len(mat[0])
        for r in range(row):
            mat[r] = [-1] + mat[r] + [-1]
        
        mat = [[-1]* (col + 2)] + mat + [[-1]* (col + 2)]
        
        path = [(-1, 0), (1,0), (0, 1), (0, -1)]
        
        for r in range(1, row +1):
            for c in range(1, col + 1):
                if all(mat[r][c] > mat[r + dr][c + dc] for dr, dc in path):
                    return (r - 1,c -1)