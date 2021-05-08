from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        presum = 0
        lst = []
        for i, a in enumerate(nums):
            presum += a
            presum %= k
            if presum not in remainder:
                remainder[presum] = i
            elif i - remainder[presum] > 1:
                return True
        return False
        