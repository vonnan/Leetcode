class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] +[nums[i] - nums[i-1] for i in range(1, n)]
        res = 1
        for i, d in enumerate(diff[1:], 1):
            if (d > 0 and diff[i-1] <=0 ) or (d < 0 and diff[i-1] >= 0):
                res += 1
            elif d == 0:
                diff[i] = diff[i-1]
        return res