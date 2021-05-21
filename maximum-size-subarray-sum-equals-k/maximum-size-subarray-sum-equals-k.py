from collections import defaultdict
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(list)
        prefix[0] =[-1]
        curr, res = 0, 0
        for i, num in enumerate(nums):
            curr += num
            if prefix[curr - k]:
                res = max(res, i - prefix[curr - k][0])
            prefix[curr].append(i)
        return res