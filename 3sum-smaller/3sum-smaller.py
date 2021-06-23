class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res, n = 0, len(nums) 
        nums.sort()
        if sum(nums[:3]) >= target:
            return 0
        
        for i, num in enumerate(nums[:-2]):
            if 3 * num >= target:
                break
            j , k = i+1, n-1
            while j < k:
                sum3 = num + nums[j] + nums[k]
                if sum3 < target:
                    res += k - j
                    j += 1
                else:
                    k -= 1
        return res
                    
                    