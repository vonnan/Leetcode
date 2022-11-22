class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dic ={"6":"9", "9":"6", "0":"0", "1":"1", "8": "8"}
        res = ""
        for c in num:
            if c not in dic:
                return False
            res = dic[c] + res
        return res == num