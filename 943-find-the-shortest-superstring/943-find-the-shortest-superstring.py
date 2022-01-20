class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        @lru_cache(None)
        def suff(w1,w2):
            m = min(len(w1), len(w2))
            for i in range(m, -1, -1):
                if w2[:i] == w1[-i:]:
                    return w2[i:]
            return w2
        
        n = len(words)
        @lru_cache(None)
        def dp(mask, i):
            if mask == (1<<n) - 1:
                return ""
            
            return min([suff(words[i], words[j]) + dp(mask | 1<<j,  j) for j in range(n) if not mask & (1 <<j)], key = len)
        
        return min([words[i] + dp(1<<i, i) for i in range(n)], key = len)