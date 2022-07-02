class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        '''
        counter_s = Counter(start)
        counter_e = Counter(end)
        if counter_s["X"] != counter_e["X"] or counter_s["L"] != counter_e["L"] or counter_s["R"] != counter_e["R"]:
            return False
        
        
        start_L, start_R = [],[]
        
        for i, c in enumerate(start):
            if c == "L":
                start_L.append(i)
            elif c == "R":
                start_R.append(i)
        print(start_L, start_R)
        
        for i, c in enumerate(end):
            if c == "L":
                if i > start_L.pop(0):
                    return False
            elif c == "R":
                if i < start_R.pop(0):
                    return False
        
        return True
        '''
        s = [i if c == 'L' else -i for i, c in enumerate(start, start=1) if c in 'RL']
        e = [i if c == 'L' else -i for i, c in enumerate(end, start=1) if c in 'RL']
        
        return len(s) == len(e) and all((i>0) == (j>0) and i >= j for i, j in zip(s,e))        
    
    
    
                
            
        
