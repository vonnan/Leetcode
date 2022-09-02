class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        sets = set(target)
        dic = defaultdict(Counter)
        
        for r, word in enumerate(words):
            for c, ch in enumerate(word):
                if ch in sets:
                    dic[ch][c] += 1
        
        
        col, n = len(words[0]), len(target)
        mod = 10 ** 9 + 7
        
        @lru_cache(None)
        def dfs(k, i):
            if i == n:
                return 1
            
            if k == col:
                return 0
            
            c = target[i]
            ans = dfs(k + 1, i)
            if dic[c][k] >0:
                ans += dfs(k + 1, i + 1) * dic[c][k]
            return ans % mod
        
        return dfs(0,0)
        
        
            
            
            
            
        
        
            