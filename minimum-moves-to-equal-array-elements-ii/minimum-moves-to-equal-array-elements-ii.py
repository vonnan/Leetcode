class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        left, right= nums[0], nums[-1]
        n, tot = len(nums), sum(nums)
        if n == 1:
            return 0
        
        res = inf
        presum = list(accumulate(nums))
        sufsum = list(accumulate(nums[::-1]))[::-1]
        
        for i in range(n-1):
            res = min(res, (i+1)*nums[i]-presum[i] + sufsum[(i+1)] - (n- (i+1))*nums[i])
        
        return res
            
            
            
        