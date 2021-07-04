class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right)//2
            ct, group = 0, 1
            for num in nums:
                if ct + num > mid:
                    group += 1
                    ct = num
                    if group > m:
                        left = mid + 1
                        break
                else:
                    ct += num
            if group <= m:
                right = mid
        return left
            
            