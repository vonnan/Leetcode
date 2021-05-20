class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right)//2
            count, curr = 1, 0
            for num in nums:
                if curr + num > mid:
                    count += 1
                    curr = num
                    if count > m:
                        break
                else:
                    curr += num
            if count > m:
                left = mid + 1
        
            else:
                right = mid
        return left
