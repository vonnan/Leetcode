class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        pairs = []
        
        n = len(s)
        
        counter = Counter([])
        
        for i in range(n):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    pairs.append((i,j))
                    counter[i, j] = 2
        
        m = len(pairs)
        
        for i in range(m-1, -1, -1):
            for j in range(i-1, -1, -1):
                si, ei = pairs[i]
                sj, ej = pairs[j]
                if sj < si and s[si] != s[sj] and ej > ei:
                    counter[sj, ej] = max(counter[sj, ej], 2 + counter[si, ei])
        
        return max(counter.values()) if counter else 0