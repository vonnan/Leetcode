from math import sqrt
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        if len(positions)<=1: return 0 
        
        def calculate(x, y): 
            ans = 0
            for a, b in positions: 
                ans += pow(pow(x-a, 2) + pow(y-b, 2), 0.5)
            return ans
        xmin, xmax = positions[0][0], positions[0][0]
        ymin, ymax = positions[0][1], positions[0][1]
        xcen, ycen = 0, 0
        N = len(positions)
        for x, y in positions: 
            xmin = min(x, xmin)
            xmax = max(x, xmax)
            ymin = min(y, ymin)
            ymax = max(y, ymax)
            xcen += x
            ycen += y
        xstep = xmax - xmin 
        ystep = ymax - ymin
        x, y = xcen/N, ycen/N
        curD = calculate(x, y)
        while pow(xstep, 2) + pow(ystep, 2) > pow(10, -15): 
            # print(x, y, xstep, ystep)
            curD = calculate(x, y)
            if curD>calculate(x+xstep, y+ystep): 
                x += xstep
                y += ystep
            elif curD>calculate(x-xstep, y+ystep): 
                x -= xstep
                y += ystep
            elif curD>calculate(x-xstep, y-ystep): 
                x -= xstep
                y -= ystep
            elif curD>calculate(x+xstep, y-ystep): 
                x += xstep
                y -= ystep
            else: 
                xstep/=2
                ystep/=2
        return curD
                
