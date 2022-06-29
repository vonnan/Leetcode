class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat), len(mat[0])
        res =[]
        
        for k in range(row+col-1):
            lst = []
            for r in range(row):
                c = k - r
                if c >= col:
                    continue
                elif c <0:
                    break
                else:
                    lst.append(mat[r][c])
            if k %2 ==0:
                res.extend(lst[::-1])
            else:
                res.extend(lst)
        
        return res
                
        