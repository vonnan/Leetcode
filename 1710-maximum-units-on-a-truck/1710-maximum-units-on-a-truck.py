class Solution:
    def maximumUnits(self, A: List[List[int]], B: int) -> int:
        A.sort(key = lambda x: x[1])
        res = 0
        while A and B:
            box, unit = A.pop()
            if B >= box:
                B-= box
                res += box * unit
            else:
                return res + B * unit
        return res