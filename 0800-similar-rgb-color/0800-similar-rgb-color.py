class Solution:
    def similarRGB(self, color: str) -> str:
        def helper(c):
            res = 0
            for k in range(1, 16):
                res = min(res, 16 * k + k, key = lambda x: abs(x - int(c, 16)))
            return hex(res)[2:].zfill(2)
        
        return "#" + "".join(helper(color[i:i+2]) for i in [1,3,5])
            