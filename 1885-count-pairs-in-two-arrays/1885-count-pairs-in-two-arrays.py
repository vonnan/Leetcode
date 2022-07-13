from bisect import bisect_left

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        nums = sorted([a - b for a, b in zip(nums1, nums2)], reverse = 1)
        nums_r = [-num for num in nums]
        res = 0
        for num in nums:
            idx = bisect_left(nums_r, num)
            res += idx
            if num > 0:
                res -= 1
        return res//2
                    
                    
        
            
            
            
                
            
            
        