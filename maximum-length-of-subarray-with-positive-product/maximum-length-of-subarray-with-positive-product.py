class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        s = ""
        for num in nums:
            if num == 0:
                s += "0"
            elif num > 0:
                s += "+"
            else:
                s += "-"
                
        
        s = s.split("0")
        res = 0
        for c in s:
            if c:
                ct = c.count("-")
                n = len(c)
                if not ct % 2:
                    res = max(res, n )
                else:
                    idx = c.index("-")
                    ridx = c.rindex("-")
                    x = max([idx, ridx, n - 1 - idx, n-1 -idx])
                    res = max(x, res)
                    
        return res
                