class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        nums = [-1, -1] + nums + [1000000, 1000000]
        #print(nums, len(nums))
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            #print(mid, nums[mid], nums[mid-1], nums[mid + 1])
            if nums[mid + 1] != nums[mid] and nums[mid - 1] != nums[mid]:
                return nums[mid]
            if nums[mid + 1] == nums[mid]:
                if mid % 2:
                    right = mid - 1
                else:
                    left = mid + 2
            else:
                if (mid - 1) % 2:
                    right = mid - 2
                else:
                    left = mid + 1
        return nums[left]
            