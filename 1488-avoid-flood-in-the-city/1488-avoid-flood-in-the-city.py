from bisect import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [-1] * n
        
        full_lake = defaultdict(list)
        dried = []
        
        for i, lake in enumerate(rains):
            if lake == 0:
                res[i] = 1
                dried.append(i)
            else:
                if lake  in full_lake:
                    if not dried:
                        return []
                    last = full_lake[lake].pop()
                    
                    if not full_lake[lake]:
                        full_lake.pop(lake)
                    
                    idx = bisect(dried, last)
                    if idx == len(dried):
                        return []
                    
                    res[dried.pop(idx)] = lake
                full_lake[lake].append(i)
                
        return res
                    
            