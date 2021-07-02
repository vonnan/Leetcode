class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        counter = Counter(nums)
        if k == 0:
            return sum(val >1 for num, val in counter.items())
        for num in sorted(counter.keys()):
            if num + k in counter:
                res += 1
        
        return res
        