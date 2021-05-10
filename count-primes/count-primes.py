class Solution:
    def countPrimes(self, n):
       
        if n<2:
            return 0
        primes = [True]*n
        primes[0] = primes[1] = False
        i = 2
        while i < int(n**0.5)+1:
            if primes:
                primes[i*i:n:i]= [False]*((n-1)//i -i+1)
            i+=1
        
        return sum(primes)
     
                        
                    
                    
            
                   
        