class Solution:
    def beautifulPartitions(self, s: str, k: int, min_: int) -> int:
        res = ""
        for c in s:
            if c in "2357":
                res += "1"
            else:
                res += "0"
        n = len(s)  
        
        if k * min_ > n or res[0] != "1" or res[-1] != "0":
            return 0
        
        lst = [0]
        mod = 10 ** 9 + 7
        for i, c in enumerate(res[1:], 1):
            if c == "1" and res[i-1] == "0":
                lst.append(i)
        
        m = len(lst)
        
        @cache
        
        def dp(i, kk):
            if kk == 1:
                return 1 if lst[i] + min_ -1 <= n -1 else 0
            
            res = 0
            
            for j in range(i + 1, m - kk + 2):
                if lst[j] - lst[i] >= min_:
                    res += dp(j, kk -1)
            
            return res % mod
        
        return dp(0, k)
                    
            
        
        
        
        