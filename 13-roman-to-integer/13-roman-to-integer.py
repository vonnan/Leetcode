class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":             1,
               "IV":            4,
               "V":             5,
               "IX":            9,
               "X":             10,
               "XL":            40,
               "L":             50,
               "XC":            90,
               "C":             100,
               "CD":            400,
               "D":             500,
               "CM":            900,
               "M":             1000}
        
        start, res = 0, 0
        n = len(s)
        while start < n:
            if s[start:start + 2] in dic:
                res += dic[s[start: start + 2]]
                start += 2
            else:
                res += dic[s[start]]
                start += 1
        return res