from bisect import bisect_left
from bisect import bisect

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        maps={"0":"0","1":"1","6":"9","8":"8","9":"6"}
        cl,ch=len(low), len(high)
        if cl>ch or (cl==ch and low>high): return 0
        
        ans=["","0","1","8"]
        count=0
        while ans:
            tmp=[]
            for w in ans:
                if len(w)<ch or (len(w)==ch and w<=high):
                    if len(w)>cl or (len(w)==cl and w>=low):  
                        if len(w)>1 and w[0]=="0":##leading zeros
                            pass
                        else:
                            count+=1
                    
                    if ch-len(w)>=2:                
                        for key in maps:
                            res=key+w+maps[key]
                            tmp.append(res)
            ans=tmp
        return count        
        
        
        
                
            
                
            
        
        