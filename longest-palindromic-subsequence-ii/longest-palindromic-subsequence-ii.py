"""
class Solution:
   
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dp(l, r, prev):
            if (l,r,prev) not in memo:
                if l >= r:
                    return 0
                if s[l] == s[r] and s[l] != prev:
                    return 2 + dp(l+1, r-1, s[l])
                memo[(l,r,prev)] = max(dp(l+1, r, prev), dp(l, r-1, prev))
            return memo[(l,r,prev)]
        
        return dp(0, len(s)-1, "")
        
        """
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        counter = defaultdict(int)
        pairs = []
        for i in range(n-1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    p = (i,j)
                    counter[p] = 2
                    pairs.append(p)
        
        m = len(pairs)
        for j in range(m-1, -1, -1):
            for i in range(j-1, -1,-1):
                p1, p2 = pairs[i], pairs[j]
                if p2[0]> p1[0] and p2[1] < p1[1] and  s[p1[0]] != s[p2[0]]:
                    counter[p1] = max(counter[p1], counter[p2] + 2)
        return max(counter.values()) if counter else 0
        
        
