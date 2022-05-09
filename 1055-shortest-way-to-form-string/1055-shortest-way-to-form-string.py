class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        start, res = 0, 1
        
        for c in target:
            if c not in source:
                return -1
            
            if c in source[start:]:
                start = source.index(c, start) + 1
            else:
                start = source.index(c) + 1
                res += 1
        
        return res