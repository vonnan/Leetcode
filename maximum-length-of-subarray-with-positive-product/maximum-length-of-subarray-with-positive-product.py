class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        lst = []
        
        for num in nums:
            if num < 0:
                lst.append("n")
            elif num >0:
                lst.append("p")
            else:
                lst.append("0")
        s = "".join(lst)
                
        def maxSub(c):
            ct_n = c.count("n")
            if ct_n %2 == 0:
                return len(c)
            else:
                res = len(c) - 1 - min(c.index("n"), c[::-1].index("n"))
                return res
            
        if "0" not in s:
            return maxSub(s)
        else:
            ls = s.split("0")
            res = 0
            for c in ls:
                res = max(res, maxSub(c))
                
        return res
            