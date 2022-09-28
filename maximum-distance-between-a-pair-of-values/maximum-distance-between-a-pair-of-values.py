class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        res = 0
        
        for i, num in enumerate(nums1):
            if i + res >= n2 - 1:
                return res
            left, right = i + res, n2 - 1
            if nums2[left] < num:
                continue
            
            while left < right:
                mid = (left + right + 1)//2
                
                if nums2[mid] < num:
                    right = mid - 1
                else:
                    left = mid
            
            
            if nums2[left] >= num:
                res = left - i
        
        return res
                
            
