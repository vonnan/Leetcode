class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        diff = [g - c for g,c in zip(gas, cost)]
        
        n = len(diff)
        presum, ct = 0, 0
        print(diff)
        diff += diff
        for i, d in enumerate(diff):
            presum += d
            if presum < 0:
                presum, ct = 0, 0
            else:
                ct += 1
                if ct == n:
                    return i - n + 1
        return -1
                
            