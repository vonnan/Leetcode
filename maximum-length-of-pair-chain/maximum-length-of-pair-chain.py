from bisect import bisect_left
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        end = pairs[0][1]
        LIS = [end]
        
        for s,e in pairs[1:]:
            if s > end:
                
                end = e
                LIS.append(end)
                
            elif e >= end:
                continue
            else:
                if len(LIS) == 1 or (len(LIS) > 1 and s > LIS[-2]):
                    end = min(LIS.pop(), e)
                    LIS.append(end)
        return len(LIS)
                
                
        