from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        candidates =[]
        for num in nums:
            idx = bisect_left(candidates, num)
            if idx == len(candidates):
                candidates.append(num)
            else:
                candidates[idx] = num
                
        return len(candidates)
            