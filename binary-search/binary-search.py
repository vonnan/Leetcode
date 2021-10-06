class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left] == target else -1