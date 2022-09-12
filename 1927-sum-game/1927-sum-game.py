class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        res = ct = 0
        for i, c in enumerate(num):
            if i < n//2:
                if c == "?":
                    ct += 1
                else:
                    res += int(c)
            else:
                if c == "?":
                    ct -= 1
                else:
                    res -= int(c)
        
        if not ct:
            if res:
                return True
            else:
                return False
        
        if res == 0:
            return True
        
        if ct %2:
            return True
        
        return res + (ct//2) * 9 != 0
        
        