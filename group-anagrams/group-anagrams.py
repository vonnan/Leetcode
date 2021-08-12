from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def converter(s):
            res = [0]*26
            for x in s:
                idx = ord(x) - 97
                res[idx] +=1
            return tuple(res)
        
        res = []
        dic = {}
        for s in strs:
            t = converter(s)
            if t not in dic:
                res.append([s])
                dic[t] = len(res)-1
            else:
                res[dic[t]].append(s)
        return res
        