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
        # Define pairs to hold list of tuples (i, j) where s[i] == s[j] and pairs[k-1][0] < pairs[k][0],
        # for all k in [1, len(pairs)-1]. That is, the pairs are sorted in increasing order by the left
        # index value i.
        pairs = []
		# Define f[p] to hold the length of the longest good palindrome subsequence starting at p[0] and
		# ending at p[1]
        f = collections.defaultdict(int)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    p = (i, j)
                    pairs.append(p)
                    f[p] = 2
        
        # Then given some pair p, we just need to find some inner pair q such that p envelopes q
        # and s[p[0]] != s[q[0]], that is the palindrome formed by extending from the indexes at q
        # with that in p would not have consecutive characters
        for j in range(len(pairs) - 1, -1, -1):
            # pairs[j] will be some inner pair
            for i in range(j - 1, -1, -1):
                # pairs[i] could be a pair of indices that envelopes pairs[j]. (At least pairs[i][0] 
                # will be < pairs[j][0]. We'll need to ensure pairs[i][1] > pairs[j][1])
                p, q = pairs[i], pairs[j]
                if p[0] < q[0] and p[1] > q[1] and s[p[0]] != s[q[0]]:
                    f[p] = max(f[p], f[q] + 2)
                    
        return max(f.values()) if len(f) else 0