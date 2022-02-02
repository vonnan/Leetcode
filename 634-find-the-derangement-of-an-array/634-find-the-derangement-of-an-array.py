class Solution:
    def findDerangement(self, n: int) -> int:
        if n== 1:
            return 0
        
        dp =[1,0]
        mod = 10**9 + 7
        
        for i in range(2, n+1):
            dp.append((dp[-1] + dp[-2])*(i-1) % mod)
        print(dp)
        return dp[-1]