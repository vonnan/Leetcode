
from collections import defaultdict
from collections import Counter
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        dic ={"a":0, "o":1, "e":2 , "i":3, "u": 4}
        dp = [[0]*5 for _ in range(len(s))]
        for i,c in enumerate(s):
            if i > 0:
                dp[i][:] = dp[i-1]
            if c in dic:
                idx = dic[c]
                dp[i][idx] = (dp[i][idx] + 1)%2
           
        dp =["".join([str(x) for x in row]) for row in dp]
        
        sets = set(dp)
        
        print(sets, dp)
        
        res, m = 0, len(dp)
        
        for item in sets:
            
            res = max(res, m-1 - dp[::-1].index(item) - dp.index(item))
            if item =="00000":
                res = max(res, m - dp[::-1].index(item))
            
        return res
        