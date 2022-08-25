class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        
        s = str(n)
        n = len(s)
        res = [int(c) for c in s]
        
        for i in range(1, n):
            if res[i] < res[i - 1]:
                while i > 0 and res[i] <= res[i-1]:
                    i -= 1
                res[i] -= 1
                res[i+ 1:] = [9] * ( n - ( i + 1))
                return int("".join([str(num) for num in res]))
        return int("".join([str(num) for num in res]))
        
        
        
        
                
            
        