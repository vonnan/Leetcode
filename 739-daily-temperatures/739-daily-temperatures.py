class Solution:
    def dailyTemperatures(self,A: List[int]) -> List[int]:
        res = [0]
        n = len(A)
        stack = [n-1]
        for i in range(n-2, -1, -1):
            a = A[i]
            while stack and a >= A[stack[-1]]:
                stack.pop()
            if not stack:
                res.append(0)
            else:
                res.append(stack[-1] - i)
            stack.append(i)
        return res[::-1]
                