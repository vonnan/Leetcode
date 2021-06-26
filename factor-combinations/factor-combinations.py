class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n == 1:
            return []
        
        res = []    
        def dfs(path = [], rest = 2, target = n):
            if len(path) > 0:
                res.append(path + [target])
            while rest * rest <= target:
                if target % rest ==0:
                    dfs(path + [rest], rest, target//rest)
                rest += 1
        
        dfs()
        return res
            