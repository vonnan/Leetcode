class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        self.res = 0
        
        def helper(nums, tmp):
            if not nums:
                self.res += 1
                
            else:
                m = len(tmp)
                for i, num in enumerate(nums):
                    if not num % (m + 1) or not (m + 1) % num:
                        helper(nums[:i] + nums[i + 1:], tmp + [num])
        
        helper(nums, [])
        return self.res
                