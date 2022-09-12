class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        counter = Counter(s)
        lst = sorted(list(counter.values()))
        
        res = 0
        if len(lst) <= 9:
            res += sum(lst)
        elif len(lst) <= 18:
            res = sum(lst[-9:]) + sum(lst[:-9]) * 2
        else:
            res = sum(lst[-9:]) + sum(lst[-18:-9]) * 2 + sum(lst[:-18]) * 3
        return res
        
            
            
        