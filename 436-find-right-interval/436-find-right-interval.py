from bisect import bisect_left
class Solution:
    def findRightInterval(self, A: List[List[int]]) -> List[int]:
        lst =sorted([[a[0], i] for i, a in enumerate(A)])
        
        res = []
        n = len(A)
        for i, a in enumerate(A):
            end = a[1]
            idx = bisect_left(lst, [end])
            if idx == n:
                res.append(-1)
            else:
                
                res.append(lst[idx][1])
                
        return res
                    
                