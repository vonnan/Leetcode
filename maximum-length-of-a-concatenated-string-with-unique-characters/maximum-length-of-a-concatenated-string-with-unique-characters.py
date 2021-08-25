class Solution:
    def maxLength(self, arr: List[str]) -> int:
        lst = [set()]
        res = 0
        
        for a in arr:
            n = len(a)
            a = set(a)
            if len(a) == n:
                for s in lst[:]:
                    s = set(s)
                    
                    if not s & a:
                        lst.append(s | a)
                        res = max(res, len(lst[-1]))
                        
                
        return res