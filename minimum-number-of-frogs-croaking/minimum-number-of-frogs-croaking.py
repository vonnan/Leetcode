class Solution:
    def minNumberOfFrogs(self, A: str) -> int:
        counter = Counter(A)
        if len(A) % 5 or sum(x not in "croak" for x in counter) > 0 or len([y for y in counter]) != 5 or len(set(y for y in counter.values())) != 1:
            return -1
        res = 0
        dp =[0]*5
        
        for i, s in enumerate(A):
            
            idx = "croak".index(s)
            dp[idx] += 1
            if s == "c":
                res = max(res, dp[0] - dp[-1])
            
            for j in range(idx):
                if dp[idx] > dp[j]:
                    return -1
        return res
            
        
        