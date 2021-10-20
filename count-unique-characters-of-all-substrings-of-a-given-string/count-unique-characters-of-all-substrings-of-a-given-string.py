class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dic = {}
        res, n = 0, len(s)
        for i, c in enumerate(s):
            if c not in dic:
                dic[c] = [-1, -1]
            j, k = dic[c]
            dic[c] = k, i
            res += (k - j) * (i - k)
        for c in dic:
            i, j = dic[c]
            res += (j-i )*(n - j)
        return res % (10** 9 + 7)
            
