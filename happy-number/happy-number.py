class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        sets = set([n])
        
        while n > 1:
            n = sum(int(c)**2 for c in str(n))
            if n in sets:
                return False
            else:
                sets.add(n)
        return True
            