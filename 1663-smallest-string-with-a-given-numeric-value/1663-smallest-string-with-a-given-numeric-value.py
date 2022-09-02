import string
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        dic = {}
        for c, i in zip(ascii_lowercase, range(1, 27)):
            dic[i] = c
        
        res = [1] * n
        k -= n
        
        q, r = divmod(k, 25)
        
        res[n-(q + 1)] += r
        if q:
            res[-q:] = [26]* q
        
        
        return "".join([str(dic[num]) for num in res])
            