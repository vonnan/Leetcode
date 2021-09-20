class Solution:
    def peopleIndexes(self, A: List[List[str]]) -> List[int]:
        lst = [set(a) for a in A]
        res, n = [], len(A)
        
        for i,a in enumerate(A):
            flag = True
            for b in (A[:i] + A[i+1:]):
                
                if len(a) < len(b):
                    if (set(a)).issubset(set(b)):
                        flag = False
                        break
            if flag:
                res.append(i)
        
        return res
        
                        
                
                    
        
        
        
        