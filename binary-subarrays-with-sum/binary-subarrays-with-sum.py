class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        lst = [0] + list(accumulate(nums))
        res = 0
        counter = Counter([])
        
        for num in lst:
            if num - goal in counter:
                res += counter[num - goal]
            counter[num] += 1
            
        return res