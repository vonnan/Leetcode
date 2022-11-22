class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        primes = ['2', '3', '5', '7']
        
        # pruning
        if k * minLength > n or s[0] not in primes or s[-1] in primes:
            return 0
        
        # posible starting indexes of a new partition
        ids = [0]
        for i in range(n-1):
            if s[i] not in primes and s[i+1] in primes:
                ids.append(i+1)
        m = len(ids)

        @cache
        # dp(i, kk) means number of ways to partition s[ids[i]:n] into kk partitions
        def dp(i, kk):
            
            # kk==1: last remaining partition, needs to have length >= l
            if kk == 1:
                return 1 if ids[i]+minLength-1 <= n-1 else 0
            res = 0
            
            # iterate possible starting index of next partition
            for j in range(i+1, m-kk+2):
                if ids[j]-ids[i] >= minLength:
                    res += dp(j, kk-1)
            
            return res % (10**9+7)
        
        return dp(0, k)
                
        