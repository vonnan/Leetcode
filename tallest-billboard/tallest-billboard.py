class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
       
        dp = defaultdict(int)
        dp[0] =0 
        for rod in rods:
            for d, r in list(dp.items()):
                dp[d + rod] = max(dp[d + rod], r)
                dp[abs(d - rod)] = max(dp[abs(d - rod)], r + min(d,rod))
        
        return dp[0]
            
        
        
        