class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic, dic_r = {}, {}
        for a, b in zip(s,t):
            if a in dic:
                if b != dic[a]:
                    return False
            elif b in dic_r:
                if dic_r[b] != a:
                    return False
            else:
                dic[a] = b
                dic_r[b] = a
        return True
                