class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        @lru_cache(None)
        
        def dp(i, k):
            if i == n:
                return 0
            if k == -1:
                return inf
            res, _max, _sum = inf, nums[i], 0
            for j in range(i, n):
                _sum += nums[j]
                if nums[j] > _max:
                    _max = nums[j]
                wasted = _max *(j-i + 1) - _sum
                res = min(res, dp(j + 1, k - 1) + wasted)
            return res
        
        return dp(0, k)
            