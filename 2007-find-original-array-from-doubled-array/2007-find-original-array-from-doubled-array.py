class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2:
            return []
        
        counter = Counter(changed)
        lst = sorted(list(counter.keys()))
        res = []
        target = n//2
        
        while target:
            last = lst.pop()
            
            if last not in counter:
                continue
            if last % 2:
                return []
            
            if last:
                val = counter.pop(last)
                if counter[last//2] < val:
                    return []
                else:
                    counter[last//2] -= val
                    res.extend([last//2] * val)
                    target -= val
                    
                    if counter[last//2] == 0:
                        counter.pop(last//2)
            else:
                val = counter.pop(0)
                if val % 2:
                    return []
                
                val //= 2
                if target == val:
                    res.extend([0] * val)
                    return res
                else:
                    return []
        return res    
            
                
                        
                        
            