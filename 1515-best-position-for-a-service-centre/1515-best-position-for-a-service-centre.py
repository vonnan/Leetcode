from math import sqrt
class Solution:
    def getMinDistSum(self, A: List[List[int]]) -> float:
        X, Y = [ x for x, _ in A], [y for _, y in A]
        n = len(A)
        
        def dist(a, b):
            return sum(sqrt(pow((x- a), 2) + pow(y - b, 2)) for x, y in A)
        
        x_min, x_max = min(X), max(X)
        y_min, y_max = min(Y), max(Y)
        x, y = sum(X)/n, sum(Y)/n
        x_step, y_step = x_max- x_min, y_max - y_min
        
        curr = dist(x, y)
        while x_step** 2 + y_step**2 > 10**(-11):
            curr = dist(x, y)
            if curr > dist(x + x_step, y + y_step):
                x += x_step
                y += y_step
            elif curr > dist(x + x_step, y - y_step):
                x += x_step
                y -= y_step
            elif curr > dist(x - x_step, y + y_step):
                x -= x_step
                y += y_step
            elif curr > dist(x - x_step, y - y_step):
                x -= x_step
                y -= y_step
            else:
                x_step /= 2
                y_step /= 2
        
        return curr
        
        
            
        
                    
