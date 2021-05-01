from collections import Counter
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        res = 0
        
        while edges:
            x, y = edges.pop()
            if x not in seen and y not in seen:
                res += 1
                seen.add(x)
                seen.add(y)
                
            for a, b in edges:
                if a in (x,y) or b in (x,y):
                    if a in seen and (b in seen):
                        continue
                    else:
                        edges.append([a,b])
                        seen.add(a)
                        seen.add(b)
                        
        return n - len(seen) + res
                        
                        
        