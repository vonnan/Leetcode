class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        if not s:
            return 0
        
        sign = ""
        
        if s[0] == "+" or s[0] == "-":
            sign = s[0]
            s = s[1:]
        
        res = ""
        for c in s:
            if c.isdigit():
                res += c
            else:
                break
        if not res:
            return 0
        res = int(res)
        if sign == "-":
            res = -res
            
        if -2**31 <= res <= 2**31 -1:
            return res
        
        elif res < -2 ** 31:
            return -2 ** 31
        
        else:
            return 2 **31 - 1