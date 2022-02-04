class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sets = set([0])
        
        for stone in stones:
            new = set([])
            for curr in sets:
                new.add(curr + stone)
                new.add(curr - stone)
            sets = new
        
        return min(abs(x) for x in sets)
            
        