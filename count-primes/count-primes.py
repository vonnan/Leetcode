class Solution:
    def countPrimes(self, n):
       
        if n<2:
            return 0
        primes = [True]*n
        primes[0] = primes[1] = False
        i = 2
        while i < int(n**0.5)+1:
            for j in range(i, n//i +1):
                if i*j < n and primes[i*j]:
                    primes[i*j] = False
            i += 1
        
        return sum(primes)
     
                        
                    
                    
            
                   
        