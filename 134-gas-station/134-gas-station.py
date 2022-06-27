class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        diff = [g - c  for g, c in zip(gas, cost)]
       
        diff += diff
        n = len(gas)
        diff = diff[::-1]
        
        presum, ct = 0, 0
        while diff:
            nxt = presum + diff.pop()
            if  nxt < 0:
                presum, ct = 0, 0
            else:
                presum = nxt
                ct += 1
                if ct == n:
                    return n - len(diff)
        return -1
                
            
        
        