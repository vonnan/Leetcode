class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cut =[i for i in range(-1, n)]
        
        for i in range(n):
            for j in range(i, n):
                if s[i:j] == s[j:i:-1]:
                    cut[j + 1] = min(cut[j + 1], cut[i] + 1)
        return cut[-1]