class Solution:
    def jump(self, nums: List[int]) -> int:
        last, res = len(nums) - 1, 0
        
        while last > 0:
            for i, num in enumerate(nums[: last + 1]):
                if i + num >= last:
                    last = i
                    break
            res += 1
            print(last, res)
        return res
                    