class Solution:
    def isHappy(self, n: int) -> bool:
        sets = set([n])
        while n != 1:
            n = str(n)
            n = sum(int(c)**2 for c in n )
            if n in sets:
                return False
            sets.add(n)
        return True