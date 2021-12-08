class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ct, start = 1, 0
        for c in target:
            start = source.find(c, start)
            if start == -1:
                start = source.find(c)
                ct += 1
                if start == -1:
                    return -1
            #print(start, ct)
            start += 1
        return ct