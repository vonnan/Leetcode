class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        dp = [[]]
        nums.sort()
        
        for num in nums:
            dp.append(max([x + [num] for x in dp if not x or num % x[-1] == 0], key = len))
        
        return max(dp, key = len)
                     