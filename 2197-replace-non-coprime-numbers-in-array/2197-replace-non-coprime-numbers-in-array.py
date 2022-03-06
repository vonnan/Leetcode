from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = [1]
        def lcm(a, b):
            return a * b //(gcd(a, b))
        
        while nums:
            while nums and nums[0] == 1:
                res.append(nums.pop(0))
            while nums and nums[0] == res[-1]:
                nums.pop(0)
            if not nums:
                return res[1:]
            g = gcd(res[-1], nums[0])
            if g == 1:
                res.append(nums.pop(0))
            else:
                a, b = res.pop(), nums.pop(0)
                g = gcd(a, b)
                lcm = a * b // g
                while g > 1:
                    lcm = a * b // g
                    g = gcd(res[-1], lcm)
                    if g > 1:
                        a = res.pop()
                        b = lcm
                        
                if g == 1:
                    res.append(lcm)
                
            
                
           
            
        return res[1:]
                
            
            