class Solution:
    def maxLength(self, arr: List[str]) -> int:
        sets = set([""])
        res = 0
        for a in arr:
            if len(a) == len(set(a)):
                for s in list(sets):
                    if len(set(a + s)) == len(a) + len(s):
                        sets.add(a + s)
                        if len(a + s) > res:
                            res = len(a + s)
        return res
                        