class Solution:
    def maxLength(self, arr: List[str]) -> int:
        sets = set([""])
        res = 0
        for a in arr:
            if len(a)== len(set(a)):
                for s in list(sets):
                    if not set(s) & set(a):
                        sets.add(s + a)
                        res = max(res, len(s) + len(a))
                        
        return res