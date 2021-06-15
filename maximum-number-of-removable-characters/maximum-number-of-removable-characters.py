class Solution:
    def maximumRemovals(self, s: str, p: str, removable):
        def check(m):
            lst = list(s)
            sets = set(removable[:m])
            j = 0
            for i,ch in enumerate(s):
                if i in sets:
                    continue
                
                if ch == p[j]:
                    j += 1
                    if j == len(p):
                        return True
                    
            return False
             
        l, r = 0, len(removable)
        while l < r:
            mid = (l+r+1)//2
            if check(mid):
                l = mid 
            else:
                r = mid - 1
        return l
        
                
                
            
       