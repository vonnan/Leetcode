class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        change = [1] * n
        for i in range(n):
            change[(i - nums[i] + 1)% n] -= 1
        
        print(change)
        
        for i in range(1, n):
            change[i] += change[i - 1]
        
        print(change)
        return change.index(max(change))