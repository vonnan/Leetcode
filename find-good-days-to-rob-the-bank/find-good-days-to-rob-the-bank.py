class Solution:
    def goodDaysToRobBank(self, A: List[int], time: int) -> List[int]:
        n = len(A)
        
        dp, dp2 = [0] * n, [0]*n
        curr = 0
        for i in range(1, n):
            if A[i] <= A[i-1]:
                curr += 1
                dp[i] = curr
            else:
                curr = 0
        
        curr = 0
        for j in range(n-2, -1, -1):
            if A[j] <= A[j+1]:
                curr += 1
                dp2[j] = curr
            else:
                curr = 0
        print(dp, dp2)
        return [i for i in range(n)  if (dp[i] >= time and dp2[i] >= time) ]
 