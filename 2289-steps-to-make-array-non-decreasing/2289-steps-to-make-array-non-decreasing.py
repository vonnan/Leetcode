class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = [(nums[0], 0)]
        res = 0
        
        for i, num in enumerate(nums[1:], 1):
            t = 0
            while stack and stack[-1][0] <= num:
                t = max(t, stack.pop()[1])
            
            if stack:
                t += 1
            else:
                t = 0
                
            res = max(res, t)
            stack.append((num, t))
        
        return res
                
                
                
        
