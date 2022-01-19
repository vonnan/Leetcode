class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        rows, cols = len(seats), len(seats[0])
        masks = []
        
        for row in seats:
            mask = sum((1<<c) * (val == ".") for c, val in enumerate(row) )
            masks.append([c for c in range(1<<cols) if ((c & mask) == c) and c & (c >> 1) == 0 ])
        
        @lru_cache(None)
        def dfs(curr, r):
            if r == -1:
                return 0
            
            res = 0
            for prev in masks[r-1]:
                if (curr >>1 ) & prev == 0 and (curr & (prev >> 1) == 0):
                    res = max(res, dfs(prev, r -1))
            
            return res + bin(curr).count("1")
        
        return max(dfs(mask, rows-1) for mask in masks[-1])