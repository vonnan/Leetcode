class Solution:
    def getMaxGridHappiness(self, m: int, n: int, iC: int, eC: int) -> int:
        LI, LE =  -30, 20
        gain = [0, 120, 40]
        
        penalty = [[0, 0, 0], [0, 2 * LI, LI + LE], [0, LI + LE, 2 * LE]]
        
        @lru_cache(None)
        def dp(index, row, I, E):
            if index == -1:
                return 0
            
            r,c = divmod(index, n)
            res = []
            
            neib =[(I, E, 0),  (I -1, E, gain[1]), (I, E-1, gain[2])]
            
            for i in range(3):
                di, de, g= neib[i]
                tmp = 0
                if di>= 0 and de >= 0:
                    tmp = dp(index -1, (i,)+ row[:-1], di, de) + g
                    if r < m-1:
                        tmp += penalty[i][row[-1]]
                    if c < n-1:
                        tmp += penalty[i][row[0]]
                res.append(tmp)
            
            return max(res)
        
        if m <n:
            m, n = n, m
            
        return dp(m * n -1, tuple([0]*n), iC, eC)
            
        
            