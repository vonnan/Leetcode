class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(m):
            if m ==1 or m==4:
                return False
            if m == 2 or m==3 or m==5:
                return True
            
            for i in range(2, int(m**0.5)+1):
                if m % i ==0:
                    return False
            
            return True
        
        if 8 <= n <= 11:
            return 11
        
        for i in range(10**(len(str(n))//2), 10**5):
            num = int(str(i)+ str(i)[-2::-1])
            if num >= n and isPrime(num):
                return num
        