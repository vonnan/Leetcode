from bisect import bisect_left
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        LIS = [ nums[0]]
        
        for num in nums[1:]:
            idx = bisect_left(LIS, num)
            if idx == len(LIS):
                LIS.append(num)
                if len(LIS) >= 3:
                    return True
            else:
                LIS[idx] = num
            
        
        return False