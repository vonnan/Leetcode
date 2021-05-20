class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key= len)
        dp = defaultdict(int)
        #dp[word]: the longest string chain forming word
        for word in words:
            for i in range(len(word)):
                dp[word] = max(dp[word[:i] + word[i+1:]]+1, dp[word])
        return max(dp.values())
        