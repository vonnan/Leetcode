"""
class Solution(object):
    def letterCasePermutation(self, S):
        
        res = [""]
        for s in S:
            if not s.isalpha():
                for i in range(len(res)):
                    res[i] += s
            else:
                for i in range(len(res)):
                    tmp = res[i]
                    res[i] += s.lower()
                    res.append(tmp + s.upper())
        return res
"""
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [""]
        for s in S:
            if not s.isalpha():
                for i in range(len(res)):
                    res[i] += s
                    
            else:
                for i in range(len(res)):
                    tmp = res[i]
                    res[i] += s.lower()
                    res.append(tmp + s.upper())
        return res
     
        