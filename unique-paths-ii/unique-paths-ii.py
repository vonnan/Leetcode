from collections import defaultdict
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = defaultdict(int)
        memo[(0,0)] = 1
        visited = set()
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for d in range(m+n-1):
            for i in range(min(d+1, m)):
                j = min(d - i, n-1)
                if obstacleGrid[i][j] ==1:
                    memo[(i,j)] = 0
                elif obstacleGrid[i][j] ==0 and (i,j) not in visited:
                    if j > 0:
                        memo[(i, j)] += memo[(i, j-1)]
                        
                    if i > 0:
                        memo[(i, j)] += memo[(i-1, j)]
                visited.add((i, j))
        return memo[(m-1, n-1)]