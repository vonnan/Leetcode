class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s) + 1
        
        #if s[i]== "I", do not change order; if s[i] == "D", decreasing order
        
        res = []
        for i, c in enumerate(s):
            if c == "I":
                res.extend(range(i + 1, len(res), -1))
        res.extend(range(n, len(res), -1))
        
        return res
       
        