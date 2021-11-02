from bisect import bisect_left
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        LIS = []
        for num in nums:
            idx = bisect_left(LIS, num)
            if idx == len(LIS):
                LIS.append(num)
            else:
                LIS[idx] = num
        return len(LIS) >= 3
        
        
        