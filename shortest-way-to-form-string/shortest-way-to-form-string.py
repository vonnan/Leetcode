class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        start, res = 0, 1
        
        for c in target:
            if c not in source:
                return -1
            if c in source[start:]:
                start += source[start:].find(c)
            else:
                start = source.find(c)
                res += 1
            start += 1
        return res
            
                