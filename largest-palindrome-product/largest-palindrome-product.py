class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n ==1:
            return 9
        
        hi, lo = 10**n -1 , 10**(n-1)
        top = hi//11*11
        
        for left in range(hi, lo-1, -1):
            res = int(str(left) + str(left)[::-1])
            
            for d in range(top, left -1, -11):
                if res % d== 0:
                    q = res//d
                    if lo <= q <= hi:
                        return res % 1337
        
            