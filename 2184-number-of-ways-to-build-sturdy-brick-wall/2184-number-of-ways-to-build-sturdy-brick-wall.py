class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        if min(bricks) > width:
            return 0
        
        bricks.sort()
        combos = []
    
        def dfs(path): 
            if path[-1] == width:
                combos.append(tuple(path[1:-1]))    
            for b in bricks:
                if path[-1] + b > width:
                    break
                else:
                    dfs(path + [path[-1] + b])
                
        path = [0]
        
        nei = defaultdict(set)
        dfs(path)
        for i, combo_i in enumerate(combos):
            for j, combo_j in enumerate(combos):
                if not (set(list(combo_i)) & set(list(combo_j))):
                    nei[i].add(j)
        mod = 10**9 + 7 
        
        dp = [1]* len(combos)
        
        for _ in range(height - 1):
            dp2 = [0] * len(combos)
            for i in range(len(combos)):
                if nei[i]:
                    dp2[i] = sum(dp[j] for j in nei[i])
        
            dp = dp2
            
        return sum(dp) % mod
                
        
        
        
    
        