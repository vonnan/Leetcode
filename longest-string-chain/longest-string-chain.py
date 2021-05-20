class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)
        for word in sorted(words, key = len):
            for i in range(len(word)):
                dp[word] = max(dp[word[:i]+word[i+1:]] + 1, dp[word])
        return max(dp.values())