class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = min(nums), max(nums)
        
        def check(avg):
            tot = sum(nums[i] - avg for i in range(k))
            if tot >=0:
                return True
            prev, prev_min = 0, 0
            for i in range(k, len(nums)):
                tot += nums[i] - avg
                prev += nums[i-k] - avg
                prev_min = min(prev_min, prev)
                if tot >= prev_min:
                    return True
                
            return False
        
        while right - left > 10**(-6):
            mid = (left + right)/2
            if check(mid):
                left = mid
            else:
                right = mid
       
        return left
                
                
                