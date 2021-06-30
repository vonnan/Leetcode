class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        stack, n, res, ct =[], len(nums), 0, 0
        
        for i, num in enumerate(nums):
            if num ==0:
                stack.append(i)
        
        if len(stack)<=1:
            return n
        
        for i, idx in enumerate(stack):
            if i ==0:
                res = max(res, stack[i+1])
            elif i == len(stack)-1:
                res = max(res, n - 1- stack[i-1])
            else:
                res = max(res, stack[i+1] - stack[i-1] -1)
                
        return res
                
                
                    
                
                
                
        