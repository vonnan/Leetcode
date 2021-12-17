class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        up, dw, lt, rt = tuple(collections.defaultdict(int) for _ in range(4))
        zeroes = set()
        for r in range(m):
            for c in range(n):
                x, y = m - r - 1, n - c - 1
                E, W = (grid[r][c] == 'E'), (grid[r][c] != 'W')
                G, K = (grid[x][y] == 'E'), (grid[x][y] != 'W')
                up[r,c] = (up[r-1,c] + E) * W
                lt[r,c] = (lt[r,c-1] + E) * W
                dw[x,y] = (dw[x+1,y] + G) * K
                rt[x,y] = (rt[x,y+1] + G) * K
                if grid[r][c] == "0": zeroes.add((r, c))
        return max([up[r,c] + dw[r,c] + lt[r,c] + rt[r,c] for r, c in zeroes] or [0])