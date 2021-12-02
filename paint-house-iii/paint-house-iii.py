class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dp(house, block, prev):
            if house == m and block == target:
                return 0
            
            if house >= m or block > target:
                return inf
            
            res = inf
            if houses[house]:
                res = dp(house + 1, block + ( houses[house] != prev), houses[house])
            else:
                for color in range(1, n+1):
                    res = min(res, cost[house][color - 1] + dp(house +1, block + (color != prev), color))
            return res 
        res =  dp(0,0, None)
        return res if res < inf else -1