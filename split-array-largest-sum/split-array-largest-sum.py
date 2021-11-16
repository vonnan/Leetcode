class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right)//2
            sum_, ct = 0, 1
            for num in nums:
                if sum_ + num > mid:
                    sum_= num
                    ct += 1
                    if ct > m:
                        break
                else:
                    sum_ += num
            if ct > m:
                left = mid + 1
            else:
                right = mid
        
        return left
                