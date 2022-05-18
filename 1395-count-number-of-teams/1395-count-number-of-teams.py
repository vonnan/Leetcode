class Solution:
    def numTeams(self, rating: List[int]) -> int:
        up, down = defaultdict(list), defaultdict(list)
        
        for num in rating:
            for prev in up:
                if num > prev:
                    up[prev].append(num)
            up[num] = []
            for prev in down:
                if num < prev:
                    down[prev].append(num)
            down[num] = []
        
        res = 0
        for num, lst in up.items():
            for val in lst:
                res += len(up[val])
        
        for num, lst in down.items():
            for val in lst:
                res += len(down[val])
        
        return res
                
        
        