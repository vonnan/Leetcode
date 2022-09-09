class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], a: int, b: int) -> int:
        n = len(nums)
        a, b = max(a, b), min(a, b)
        dp_a, dp_b = [0] * (n - a + 1), [0] * (n - b + 1)
        
        prefix = sum(nums[:a])
        dp_a[0] = prefix
       
        for i in range(n - a):
            prefix -= nums[i]
            prefix += nums[i + a]
            dp_a[i+1] = prefix
        
        prefix = sum(nums[:b])
        dp_b[0] = prefix
        
        for i in range(n - b):
            prefix -= nums[i]
            prefix += nums[i + b]
            dp_b[i+1] = prefix
            
        res = 0
        
        for i, num in enumerate(dp_a):
            num_b = 0
            if i > b:
                num_b = max(num_b, max(dp_b[:i - b + 1]))
            if i + a + b<= n:
                num_b = max(num_b, max(dp_b[i+a:]))
            res = max(res, num + num_b)
        return res
                
            
        