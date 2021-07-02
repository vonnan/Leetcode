class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [""] * numRows
        idx, step = 0, 1
        if numRows == 1 or len(s) <= numRows:
            return s
        
        for ch in s:
            res[idx] += ch
            if idx == 0:
                step = 1
            elif idx == numRows -1:
                step = -1
            idx += step
        return "".join(res)
        