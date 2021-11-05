class Solution:
    def minAvailableDuration(self, A: List[List[int]], B: List[List[int]], d: int) -> List[int]:
        A = [(s, e) for s, e in A if e - s >= d]
        B =  [(s, e) for s, e in B if e - s >= d]
        C = sorted(A + B)
        if not C:
            return []
        start, end = C[0]
        for i in range(1, len(C)):
            s, e = C[i]
            if s > end - d:
                start, end = s, e
                continue
            else:
                return [s, s + d]
        return []