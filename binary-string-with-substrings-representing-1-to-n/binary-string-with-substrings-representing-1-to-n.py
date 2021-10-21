class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if n==1:
            if "1" in s:
                return True
            else:
                return False
        for i in range(n, n//2-1, -1):
            if bin(i)[2:] not in s:
                return False
        return True