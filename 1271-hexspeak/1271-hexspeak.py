class Solution:
    def toHexspeak(self, num: str) -> str:
        num = int(num)
        res = ""
        dic = {0: "O", 
               1: "I", 
               10: "A",
               11: "B",
               12: "C", 
               13: "D", 
               14: "E", 
               15: "F"}
        while num:
            num, r = divmod(num, 16)
            if r not in dic:
                return "ERROR"
            res = dic[r] + res
        return res
        