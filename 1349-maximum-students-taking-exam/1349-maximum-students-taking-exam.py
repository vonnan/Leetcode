class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        rows, cols = len(seats), len(seats[0])
        
        masks = []
        
        for row in seats:
            mask = sum(1<< j for j in range(cols) if row[j] == ".")
            masks.append([c for c in range(1 << cols) if c & mask == c and c & (c >>1) ==0])
            
        @lru_cache(None)
        def dp(mask, r):
            if r == -1:
                return 0
            
            res = 0
            for prev in masks[r-1]:
                if mask & (prev >>1) ==0 and prev & (mask >>1) == 0:
                    res = max(res, dp(prev, r -1))
            return res + bin(mask).count("1")
        
        return max(dp(mask, rows - 1) for mask in masks[-1])
            
            