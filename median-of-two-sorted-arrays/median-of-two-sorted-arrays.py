class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                nums.append(nums1.pop(0))
            else:
                nums.append(nums2.pop(0))
                
        if nums1 or nums2:
            nums.extend(nums1 or nums2)
        
        n = len(nums)
        if n %2:
            return nums[n//2]
        else:
            return (nums[n//2] + nums[n//2 - 1])/2