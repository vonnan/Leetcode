class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        n = len(strs[0])
        sets = set([])
        pre = ""
        for c in strs[0]:
            pre += c
            sets.add(pre)
        
        for s in strs[1:]:
            new = set([])
            pre = ""
            for c in s[:n]:
                pre += c
                if pre in sets:
                    new.add(pre)
            if not new:
                return ""
            sets = new
        return sorted(sets, key = len)[-1] if sets else ""
                