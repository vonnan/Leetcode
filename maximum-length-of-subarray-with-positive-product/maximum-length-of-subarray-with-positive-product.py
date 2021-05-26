class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        lst = []
        for num in nums:
            if num <0:
                lst.append("n")
            elif num > 0:
                lst.append("p")
            else:
                lst.append("0")
                
        s = "".join(lst)
        def maxSub(c):
            ct = c.count("n")
            if ct%2 ==0:
                return len(c)
            else:
                return len(c) - 1 - min((c.index("n"), c[::-1].index("n")))
            
        if "0" not in s:
            return maxSub(s)
        else:
            lst = s.split("0")
            res = 0 
            for c in lst:
                if c:
                    res = max(res, maxSub(c))
                    
            return res
                                        
                                        
                