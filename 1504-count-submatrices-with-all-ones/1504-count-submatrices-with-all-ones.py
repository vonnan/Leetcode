class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        
        for r in range(row):
            for c in range(1, col):
                if mat[r][c]:
                    mat[r][c] = mat[r][c-1] + 1
        
        res = 0
        for r in range(row):
            for c in range(col):
                if mat[r][c]:
                    prev = mat[r][c]
                    for t in range(r, -1, -1):
                        if not mat[t][c]:
                            break
                        prev = min(prev, mat[t][c])
                        res += prev
        
        return res
                        