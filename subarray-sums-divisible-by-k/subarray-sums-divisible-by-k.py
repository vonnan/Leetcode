from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        nums = [ num%k for num in nums]
        curr, res = 0, 0
        
        for num in nums:
            curr += num
            curr %= k
            res += prefix[curr]
            prefix[curr] += 1
        
        return res