class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        counter = Counter(nums)
        
        if k == 0:
            return sum(val > 1 for val in counter.values())
        
        for key in sorted(counter.keys()):
            if key + k in counter:
                res += 1
                
        return res
            
        