class Solution:
    def maximum69Number (self, nums: int) -> int:
        nums = str(nums)
        res = ""
        for i, num in enumerate(nums):
            if num == "6":
                res += "9"
                break
            res += num
        return res + nums[i+1:]
                