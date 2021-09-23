class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        last, res = n-1, 0
        while last > 0:
            for i in range(last+1):
                if i + nums[i] >= last:
                    last = i
                    break
            res += 1
        return res