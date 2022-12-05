class Solution:
    def totalSteps(self, A: List[int]) -> int:
        n = len(A)
        dp = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[i] > A[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
            stack.append(i)
        return max(dp)
        