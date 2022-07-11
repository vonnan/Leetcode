
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        # for each number, compute how many branches it can have. Then for each of those branches
        # compute how many branches they have
        # r = 0
        # for k in range(1, maxValue+1):
        #     r += maxValue // k
        # return r
        MOD = 1000000007
        @cache
        def rec(i, k):
		    # i: current number; k: increase count
            m = comb(n-1, k-1) % MOD  # combination if the sequence stops here
            if k == n:  # no more chance to increase; sequence stops here
                return m % MOD
            for j in range(i+i, maxValue+1, i):
                m += rec(j, k+1) % MOD
            return m % MOD
        
        m = 0
        for i in range(1, maxValue+1):
            m += rec(i, 1) % MOD
        return m % MOD
