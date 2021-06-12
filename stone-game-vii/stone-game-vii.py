class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        presum = [0]
        for s in stones:
            presum.append(presum[-1] + s)
        
        @lru_cache(2000)
        
        def max_diff(i,j):
            if i > j:
                return 0
            
            pop_first = presum[j+1] - presum[i+1]
            pop_last = presum[j] - presum[i]
            
            return max(pop_first- max_diff(i+1, j), pop_last - max_diff(i, j-1))
        
        return max_diff(0, len(stones)-1)