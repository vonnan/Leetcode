from collections import Counter
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = Counter()
        
        def dp(w1, w2, i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            
            elif i ==m and j == n:
                return 0
            
            elif i == m:
                return n-j
            
            elif j == n:
                return m - i
            
            elif w1[i] == w2[j]:
                ct = dp(w1, w2, i+1, j+1)
                
            else:
                insert = dp(w1, w2, i, j+1)
                delete = dp(w1, w2, i+1, j)
                replace = dp(w1, w2, i+1, j+1)
                ct = 1 + min(insert, delete, replace)
            memo[(i, j)] = ct
            return ct
                
        return dp(word1, word2, 0, 0)
                
            
             
                