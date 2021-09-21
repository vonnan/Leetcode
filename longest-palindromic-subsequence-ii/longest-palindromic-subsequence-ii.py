class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        pairs = []
        
        counter, n = Counter(), len(s)
        
        for i in range(n):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    pairs.append((i, j))
                    counter[i,j] = 2
       
        m = len(pairs)
        for i in range(m-1, -1, -1):
            for j in range(i-1, -1, -1):
                s1, e1 = pairs[i]
                s2, e2 = pairs[j]
                #s2 <= s1
                if s2 < s1 and s[s2] != s[s1] and e2 > e1:
                    counter[s2, e2] = max(counter[s2, e2], 2 + counter[s1, e1])
                   
        
        return max(counter.values()) if counter else 0
                    
     