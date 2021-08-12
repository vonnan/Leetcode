class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod = 10**9 + 7
        memo = {}
        def dp(i,j):
            if (i, j) not in memo:
                if i > j:
                    memo[(i,j)] = 0
                elif i == j:
                    memo[(i,j)] = 1
                
                else:
                    count, seg = 0, s[i: j+1]
                    
                    for ch in "abcd":
                        idx = seg.find(ch)
                        idx_r = seg.rfind(ch)
                        if idx == idx_r == -1:
                            continue
                        else:
                            count += dp(i + idx + 1, i + idx_r -1) + 2 if idx != idx_r else 1
                    memo[(i, j)] = count%mod
            
            return memo[(i,j)]
        
        return dp(0, len(s)-1)
            
            
            
        