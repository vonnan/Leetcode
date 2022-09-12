class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        counter = Counter(s)
        lst = sorted(list(counter.values()), reverse = 1)
        
        res = 0
        ct = 0
        for i, val in enumerate(lst):
            if i % 9 ==0:
                ct += 1
            res += val * ct
        return res
    
            
            
        