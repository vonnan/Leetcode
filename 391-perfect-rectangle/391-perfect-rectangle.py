class Solution:
    def isRectangleCover(self, A: List[List[int]]) -> bool: 
        counter = Counter([])
        
        area = []
        for a,b,c,d in A:
            area.append((c-a) *(d-b))
            counter[(a,b)] += 1
            counter[(c,d)] += 1
            counter[(a,d)] += 1
            counter[(c,b)] += 1
            
        tot = sum(area)
        lst = sorted(list(counter.keys()))
        
        a,b = lst[0]
        c,d = lst[-1]
        if tot != (d-b) *(c-a):
            return False
        
        sets = set([(a,b), (c,d), (a,d), (c,b)])
        
        for key in lst:
            if key in sets:
                if counter[key] != 1:
                    return False
            else:
                if (counter[key] != 2) and (counter[key] != 4):
                    return False
                
        return True
        
        
        
                