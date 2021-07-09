class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def check(m):
            i, cursum, ct = 0, 0, 0
            for j, num in enumerate(nums):
                cursum += num
                while cursum > m:
                    cursum -= nums[i]
                    i += 1
                ct += j - i + 1
            return ct
        
        left, right = min(nums), sum(nums)
        while left < right:
            mid = (left + right)//2
            if check(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left