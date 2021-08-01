import math
class Solution:
    def minimumPerimeter(self, A: int) -> int:
        x = math.ceil((A/4)**(1/3))
        while 2*x*(2*x+1)*(x+1) >= A:
            x-=1
        x += 1
        return 8*x
    
    