class Solution:
    def findAndReplacePattern(self, words: List[str], A: str) -> List[str]:
        n = len(A)
        def helper(word):
            dic, dic_r = {}, {}
            for i, c in enumerate(word):
                if c not in dic:
                    dic[c] = A[i]
                    if A[i] in dic_r:
                        return False
                    else:
                        dic_r[A[i]] = c
                else:
                    if dic[c] != A[i] or (A[i] not in dic_r) or (dic_r[A[i]] != c):
                        return False
            return True
        
        res = []
        for word in words:
            if helper(word):
                res.append(word)
        
        return res
                
            
