class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        dp = defaultdict(int)
        
        for word in words:
            n = len(word)
            for i in range(n):
                prev = word[:i] + word[i+1:]
                dp[word] = max(dp[prev] + 1, dp[word])
            
        return max(dp.values())