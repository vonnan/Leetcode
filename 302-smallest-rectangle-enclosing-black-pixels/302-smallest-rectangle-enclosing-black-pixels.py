class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        A= ["".join(row) for row in image]
        row = len(A)
        r_min, c_min = inf, inf
        r_max, c_max = 0, 0
        for r, s in enumerate(A):
            if "1" in s:
                r_min = min(r, r_min)
                left, right = s.find("1"), s.rfind("1")
                c_min = min(c_min, left)
                c_max = max(c_max, right)
                r_max = max(r, r_max)

        return(r_max - r_min + 1) * (c_max - c_min + 1)