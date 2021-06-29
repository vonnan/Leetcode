class Solution:
    #def largestNumber(self, cost: List[int], target: int) -> str:
    def largestNumber(self, cost, target):
        memo = {}
        
        def dp(idx, remain):
            if (idx, remain) in memo:
                return memo[(idx, remain)]
            
            if idx == len(cost) or remain <0:
                return -inf
            
            if remain == 0:
                return 0
            
            ans1 = dp(idx, remain - cost[idx]) * 10 + idx + 1
            ans2 = dp(idx + 1, remain)
            
            res = max(ans1, ans2)
            
            memo[(idx, remain)] = res
            
            return res
        
        res = dp(0, target)
        
        return str(res) if res > 0 else "0"