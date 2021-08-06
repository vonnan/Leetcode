class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        max_sofar, n = 0, len(nums)
        
        for i in range(n-k +1):
            if nums[i] > max_sofar:
                max_sofar = nums[i]
                res = nums[i: i + k]
        return res
            