class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_ = -inf
        
        stack = []
        
        for num in nums[::-1]:
            if num < min_:
                return True
            
            while stack and num > stack[-1]:
                min_ = stack.pop()
            
            stack.append(num)
        
        return False
