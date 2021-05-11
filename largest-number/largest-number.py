import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if set(nums) == {0}:
            return "0"
        nums = [str(num) for num in nums]
        nums = sorted(nums, key = functools.cmp_to_key(lambda x, y: int(y+x)-int(x+y)))
        return "".join(nums)
        