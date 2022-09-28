class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right)//2
            
            ct = 1
            tot = 0
            for num in nums:
                if tot + num <= mid:
                    tot += num
                else:
                    tot = num
                    ct += 1
                    if ct > m:
                        break
            if ct > m:
                left = mid + 1
            else:
                right = mid
        
        return left