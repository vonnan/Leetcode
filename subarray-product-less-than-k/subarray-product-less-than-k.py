class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        product = 1
        j = 0
        
        for i, num in enumerate(nums):
            if num >= k:
                product = 1
                j = i + 1
                continue
            
            product *= num
            
            
            while product >= k:
                product/= nums[j]
                j += 1
            res += i - j + 1
                
        return res
                    
                        
            