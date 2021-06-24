class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack, n = [], len(nums)
        res = []
        
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num and len(stack) + n-i >k:
                stack.pop()
            stack.append(i)
            
        return [nums[i] for i in stack][:k]
        
        