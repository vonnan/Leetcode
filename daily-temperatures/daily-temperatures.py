class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        n = len(T)
        
        res = []
        for i in range(n-1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            
            if not stack:
                res.append(0)
            else:
                res.append(stack[-1] - i)
            
            stack.append(i)
            
        return res[::-1]