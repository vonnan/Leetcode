class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a,b):
            return abs(a//6 - b//6) + abs(a % 6 - b % 6)
        
        word = [ord(c) - ord("A") for c in word]
        
        dp = [0] * 26
        
        for b, c in zip(word, word[1:]):
            dp[b] = max(dp[a] + dist(b, c) - dist(a,c) for a in range(26))
            
        return sum(dist(b,c) for b,c in zip(word, word[1:])) - max(dp)
        