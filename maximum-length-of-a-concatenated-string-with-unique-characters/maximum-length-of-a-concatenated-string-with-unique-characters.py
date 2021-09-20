class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [x for x in arr if len(x) == len(set(x))]
        sets = set(arr)
        if not arr:
            return 0
        res = max(len(a) for a in arr)
        for a in arr:
            for b in list(sets):
                if not (set(a) & set(b)):
                    sets.add(a + b)
                    res = max(res, len(a) + len(b))
                    
                    
        return res
                
                    
        