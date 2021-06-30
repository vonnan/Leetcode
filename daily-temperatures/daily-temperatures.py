class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = len(temperatures)
        res = [0] * days
        
        stack = []
        
        for i in range(days-1, -1, -1):
            t = temperatures[i]
            while stack and temperatures[stack[-1]] <= t:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        
        return res