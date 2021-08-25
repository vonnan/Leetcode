class Solution:
    def maxLength(self, arr: List[str]) -> int:
        sets = set([""])
        res = 0
        
        for a in arr:
            if len(set(a)) == len(a):
                for s in list(sets):
                    if len(set(a + s)) == len(a) + len(s):
                        sets.add(a + s)
                        res = max(res, len(a + s))
        return res