class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        self.res = 0
        
        def helper(nums, pos):
            if not nums:
                self.res += 1
            else:
                for i, num in enumerate(nums):
                    if num % pos == 0 or (pos % num == 0):
                        helper(nums[:i] + nums[i+1:], pos + 1)
        
        helper(nums, 1)
        return self.res