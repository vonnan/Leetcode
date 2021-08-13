class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        word = word1 + word2
        n1, n = len(word1), len(word)
        
        @lru_cache(None)
        def dp(i,j):
            if i >= j:
                return i == j
            if word[i] == word[j]:
                return dp(i+1, j-1) + 2
            else:
                return max(dp(i, j-1), dp(i + 1, j))
        ans = 0   
        for x in set(word):
            idx = word1.find(x)
            jdx = word2.rfind(x)
            if idx != -1 and jdx != -1:
                ans = max(ans, dp(idx, jdx + n1))
        return ans
                
        