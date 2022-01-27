class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        memo = {}
        
        def dfs(w1, w2, r, c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r==m and c==n:
                return 0
            
            elif c==n:
                return m - r
            
            elif r == m:
                return n - c
            
            elif (r,c) not in memo:
                if w1[r] == w2[c]:
                    ct = dfs(w1,w2, r+1, c+1)
                    
                else:
                    insert = dfs(w1,w2, r, c+ 1)
                    delete = dfs(w1, w2, r+1, c)
                    replace = dfs(w1,w2, r+1, c+ 1)
                    ct = 1 + min(insert, delete, replace)
                memo[(r,c)] =ct
                return ct
        
        return dfs(word1, word2, 0, 0)
                    
            