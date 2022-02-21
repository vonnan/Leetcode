from math import gcd
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ct = Counter([gcd(num, k) for num in nums])
        
        lst = sorted(ct.keys())
        print(ct, lst)
        res = 0
        for i, a in enumerate(lst):
            for j, b in enumerate(lst[i:],i):
                if a == b and a **2 %k==0:
                    res += ct[a] * (ct[a] - 1)//2
                else:
                    if b * a % k== 0:
                        res += ct[a] * ct[b]
        return res
                    
          
    