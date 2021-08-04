
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        invalid = {}
        for i in range(1, 9):
            for j in range( i +1, 10):
                if (i+j + 1) % 2:
                    invalid[(i, j)] = (i + j)//2
                    invalid[(j, i)] = (i + j)//2
        
        lst = ((1,5), (2, 4), (2, 6), (3, 5), (5, 7), (5, 9), (4,8), (6, 8))
        for x, y in lst:
            del invalid[(x,y)]
            del invalid[(y, x)]
        
        seen = set()
        def dfs(curr, remain):
            if remain == 0:
                return 1
            res = 0
            seen.add(curr)
            for i in range(1, 10):
                if i not in seen and ((curr, i) not in invalid or invalid[(curr, i)] in seen):
                    res += dfs( i, remain -1)
            seen.discard(curr)
            return res
        
        return sum(dfs(1, i-1) *4 + dfs(2, i -1) * 4 + dfs(5, i -1) for i in range(m, n+1))
        
            
        
        