class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        dic = defaultdict(list)
        for r in range(row):
            for c in range(col):
                dic[c-r].append(mat[r][c])
                
        for key in dic:
            dic[key].sort(reverse = 1)
            
        for r in range(row):
            for c in range(col):
                mat[r][c] = dic[c - r].pop()
            
        return mat
                