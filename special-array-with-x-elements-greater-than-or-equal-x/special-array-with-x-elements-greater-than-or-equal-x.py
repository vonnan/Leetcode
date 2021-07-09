class Solution:
    def specialArray(self, nums: List[int]) -> int:
        left, right = 0, 1000
        while left < right:
            mid = (left + right)//2
            if sum(num >= mid for num in nums) > mid:
                left = mid + 1
            else:
                right = mid
        if sum(num >= left for num in nums) == left:
            return left
        return -1