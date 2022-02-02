from itertools import combinations
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dic = defaultdict(list)
        dic_pair = defaultdict(set)
        
        for r in range(row):
            dic[r] = [c for c in range(col) if grid[r][c] == 1]
            if len(dic[r]) >1:
                for a,b in combinations(dic[r], 2):
                    dic_pair[a,b].add(r)
        
        return sum(len(val) * (len(val)-1)//2 for val in dic_pair.values() if len(val) > 1)
            
                
        
        