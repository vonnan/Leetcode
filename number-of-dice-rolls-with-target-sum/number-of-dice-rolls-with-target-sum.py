class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dic = defaultdict(defaultdict)
        dic[1] = {i:1 for i in range(1, f+1)}
        for r in range(2, d+1):
            temp = defaultdict(int)
            for num, val in dic[r-1].items():
                for i in range(1, f+1):
                    temp[num + i] += val
            dic[r] = temp
        
        return dic[d][target] % (10**9 +7) if target in dic[d] else 0