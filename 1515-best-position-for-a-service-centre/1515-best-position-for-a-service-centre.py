from math import sqrt
class Solution:
    def getMinDistSum(self, A: List[List[int]]) -> float:
        X, Y = [ x for x, _ in A], [y for _, y in A]
        
        x_min, x_max = min(X), max(X)
        y_min, y_max = min(Y), max(Y)
        
        def dist(a, b):
            return sum(sqrt(pow((x- a), 2) + pow(y - b, 2)) for x, y in A)
        
        step = 9
        grid = [[0]* step for _ in range(step)]
        min_ = [inf, 0, 0]
        
        for _ in range(100):
            for i, row in enumerate(grid):
                for j, _ in enumerate(row):
                    x = x_min + i/step*(x_max - x_min)
                    y = y_min + j/step*(y_max - y_min)
                    cost = [dist(x,y), x, y]
                    min_ = min(min_, cost)
            x_min, x_max = min_[1] - (x_max - x_min)/3, min_[1] + (x_max - x_min)/3
            y_min, y_max = min_[2] - (y_max - y_min)/3, min_[2] + (y_max - y_min)/3
        
        return min_[0]
                    
