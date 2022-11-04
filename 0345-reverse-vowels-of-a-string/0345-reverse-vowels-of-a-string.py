class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = [c for c in s if c in "aoieuAOIEU"]
        res = ""
        for c in s:
            if c not in "aoieuAOIEU":
                res += c
            else:
                res += lst.pop()
        return res