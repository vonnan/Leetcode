class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss, tt = "", ""
        ct = 0
        for c in s[::-1]:
            if c== "#":
                ct += 1
            elif ct ==0:
                ss = c + ss
            elif ct !=0:
                ct -= 1
        ct = 0
        
        for c in t[::-1]:
            if c== "#":
                ct += 1
            elif ct ==0:
                tt = c + tt
            elif ct !=0:
                ct -= 1
        
        return ss == tt
            
        
        