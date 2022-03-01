class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(None)
        def bfs(x,y):
            if x + y == 0:
                return 0
            if x + y ==2:
                return 2
            return min(bfs(abs(x-1), abs(y-2)), bfs(abs(x-2), abs(y-1))) + 1
        x, y = abs(x), abs(y)
        return bfs(x,y)
            
            