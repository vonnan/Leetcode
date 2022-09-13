class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        flipped = set([])
        self.res = inf
        
        def helper(flips):
            flag = False
            for r in range(row):
                for c in range(col):
                    if grid[r][c] and r not in flipped and 20 + c not in flipped:
                        flipped.add(r)
                        flipped.add(20 + c)
                        flag = True
                        helper(flips + 1)
                        flipped.remove(r)
                        flipped.remove(20 + c)
            
            if not flag:
                self.res = min(self.res, flips)
            
        helper(0)
        return self.res
                    
        
        
          
        
        
        