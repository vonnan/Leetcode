class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row, col = len(grid), len(grid[0])
        
        res = list(range(col))
        for rows in grid:
            nxt = []
            for c in res:
                if c == -1:
                    nxt.append(-1)
                elif (c== 0 and rows[c] == -1) or ( c== col-1 and rows[c] == 1):
                    nxt.append(-1)
                elif rows[c] == 1 and rows[c + 1] == 1:
                    nxt.append(c+ 1)
                elif rows[c] == -1 and rows[c - 1] == -1:
                    nxt.append(c - 1)
                else:
                    nxt.append(-1)
            print(res, nxt)
            res = nxt
        return res
                
                    
                    
            