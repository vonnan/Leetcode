from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curr = 0
        res = 0
        
        for num in nums:
            curr += num
            res += prefix[curr - k]
            prefix[curr] += 1
            
        return res
            