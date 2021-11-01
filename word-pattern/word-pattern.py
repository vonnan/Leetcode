class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        
        dic = {}
        dic_r = {}
        for c in pattern:
            x = s.pop(0)
            if c not in dic and x not in dic_r:
                dic[c] = x
                dic_r[x] = c
            else:
                if c in dic and dic[c] != x:
                    return False
                if x in dic_r and dic_r[x] != c:
                    return False
        return True
        
                