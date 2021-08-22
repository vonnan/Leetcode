from bisect import bisect_left
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        sets = {0}
        tot = 0
        for r in range(len(mat)):
            mat[r].sort()
            tot += mat[r][0]
        
        if target <= tot:
            return tot - target
        
        else:
            res = target - tot
            
        for row in mat:
            
            sets = {num + prev for num in row for prev in sets}
        
        return min(abs(num - target) for num in sets)
            

        
        
        
        