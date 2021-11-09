class Solution:
    def eraseOverlapIntervals(self, A: List[List[int]]) -> int:
        A.sort(key= lambda x: x[1])
        start, end = A[0]
        res = 0
        for s, e in A[1:]:
            if s < end:
                res += 1
            else:
                start, end = s, e
        return res