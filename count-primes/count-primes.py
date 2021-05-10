class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * n
        if n <=2:
            return 0
        prime[0] = prime[1] = False
        if n <= 4:
            return sum(prime)
        i = 2
        while i <= int(n**0.5):
            if prime:
                prime[i*i: n: i] = [False]*((n-1)//i - i + 1)
            i+= 1
        
        return sum(prime)
            
                
        
        