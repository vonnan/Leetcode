class Solution:
    def newInteger(self, n: int) -> int:
        res = ""
        while n:
            n , r = divmod(n, 9)
            res = str(r) + res
            print(n,r, res)
        
        return int(res)