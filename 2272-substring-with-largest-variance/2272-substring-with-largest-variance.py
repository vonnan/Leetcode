class Solution:
    def largestVariance(self, s: str) -> int:
        sets = set(s)
        
        def kadane(a, b):
            check = False
            ct_a, ct_b = 0, 0
            ans = 0
            
            for c in s:
                if c != a and c != b:
                    continue
                    
                elif c == a:
                    ct_a += 1
                else:
                    ct_b += 1
                    
                if ct_b > ct_a:
                    ct_b = 0
                    ct_a = 0
                    check = True
                else:
                    if ct_b > 0:
                        ans = max(ans, ct_a - ct_b)
                    elif ct_b == 0 and check:
                        ans = max(ans, ct_a - 1)
            
            return ans
        
        res = 0
        for a in sets:
            for b in sets:
                if b != a:
                    res = max(res, kadane(a, b))
        
        return res
                    
                    
                
        