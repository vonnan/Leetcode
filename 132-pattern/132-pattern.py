class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        left = [inf]
        min_ = nums[0]
        
        for num in nums[1:]:
            left.append(min_)
            min_ = min(min_, num)
            
        stack = []
        for j in range(n-1, -1, -1):
            min_, num = left[j], nums[j]
            if num <= min_:
                continue
            while stack and stack[-1] <= min_:
                stack.pop()
            if stack and stack[-1] < num:
                return True
            stack.append(num)
        return False
        
        
        
                    
            