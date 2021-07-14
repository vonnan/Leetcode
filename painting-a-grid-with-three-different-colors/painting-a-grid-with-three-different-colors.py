from itertools import product
from collections import Counter
from collections import defaultdict

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7
        dic = defaultdict(list)
        
        perm = [p for p in product([1,2,3], repeat = m) if all(x!=y for x,y in zip(p, p[1:]))]
        
        for p1,p2 in product(perm, perm):
            if all(x!= y for x,y in zip(p1, p2)):
                dic[p1].append(p2)
        
        dp = Counter(perm)
        
        for _ in range(n-1):
            dp2 = Counter()
            for p1 in dic:
                for p2 in dic[p1]:
                    dp2[p2] = (dp2[p2] + dp[p1] ) % mod
        
            dp = dp2
            
        return sum(dp.values()) % mod
            
            
            