class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        num = sum(int(c) for c in str(min(nums)))% 2
        return 1- num
        
        