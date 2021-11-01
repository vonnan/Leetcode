class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def helper(word):
            res = []
            for i, w in enumerate(word):
                if i ==0 or (i > 0 and w != word[i-1]):
                    res.append(w)
                else:
                    res[-1] += w
            return res
        
        s = helper(s)
        n = len(s)
        
        res, lst = 0, []
        
        for word in words:
            word = helper(word)
            if len(word) != n:
                continue
            
            flag = True
            for i in range(n):
                if s[i][0] == word[i][0] and (len(s[i]) == len(word[i]) or (len(s[i]) > len(word[i]) and len(s[i])>= 3)):
                    continue
                else:
                    flag = False
                    break
            if flag:
                res += 1
                lst.append("".join(word))
        
        return res
                
                    