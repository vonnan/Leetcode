class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        if min(bricks) > width:
            return 0
        
        bricks.sort()
        
        options = []
    
        def dfs(path): 
            if path[-1] == width:
                options.append(tuple(path[1:-1]))
                
            for b in bricks:
                if path[-1] + b <= width:
                
                    dfs(path + [path[-1] + b])
        path = [0]
        
        nei = defaultdict(set)
        dfs(path)
        for i, combo_i in enumerate(options):
            for j, combo_j in enumerate(options):
                
                if not (set(list(combo_i)) & set(list(combo_j))):
                    nei[i].add(j)
        mod = 10**9 + 7 
        
        dp = [1]* len(options)
        
        for _ in range(height - 1):
            dp2 = [0] * len(options)
            for i in range(len(options)):
                dp2[i] = sum(dp[j] for j in nei[i])
        
            dp = dp2
            
        return sum(dp) % mod
                
        
        
        
    
        