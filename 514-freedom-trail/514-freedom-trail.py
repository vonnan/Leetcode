from bisect import bisect_left
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        dic = defaultdict(list)
        for i, c in enumerate(ring):
            dic[c].append(i)
            
        def dist(a, b):
            d = abs(a - b)
            return min(d, n - d)
        
        state = {0 : 0}
        for c in key:
            nxt = defaultdict(int)
            for i in dic[c]:
                nxt[i] = inf
                for pos in state:
                    nxt[i] = min(nxt[i], state[pos] + dist(i, pos))
            state = nxt
        
        return min(state.values()) + len(key)
                
        
              
                
            
                