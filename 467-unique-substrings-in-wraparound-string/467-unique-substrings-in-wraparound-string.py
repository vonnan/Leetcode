class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dic = {c: 1 for c in p}
        ct = 1
        for a, b in zip(p, p[1:]):
            if (ord(b) - ord(a))% 26 ==1:
                ct += 1
            else:
                ct = 1
            dic[b] = max(dic[b], ct)
        return sum(dic.values())
                
                
                
                
        