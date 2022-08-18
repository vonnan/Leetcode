class Solution:
    def similarRGB(self, color: str) -> str:
        first, second, third = color[1:3], color[3:5], color[5:7]
        res = []
        #print(hex(241)[2:], hex(238)[2:0])
        
        def change(c):
            
            if c[0] == c[1]:
                return c
            else:
                c0, c1 = int(c[0], 16), int(c[1], 16)
                if c0 < c1:
                    left, right = c0*16 + c0, (c0 + 1)* 16 + (c0 + 1)
                else:
                    left, right = (c0 - 1)* 16 + (c0 -1), c0 * 16 + c0
                
                c = int(c, 16)
                if c - left < right - c:
                    return hex(left)[2:].zfill(2)
                
                else:
                    return hex(right)[2:].zfill(2)
            
            return "#" + change(first) + change(second) + change(third)
                
                
        
        return "#" + change(first) + change(second) + change(third)
            