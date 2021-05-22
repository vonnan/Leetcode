from collections import Counter
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        n = len(pattern)
        res = []
        
        for word in words:
            if len(word) != n:
                continue
            
            dic_wp = {}
            dic_pw = {}
            flag = True
            for i in range(n):
                if word[i] not in dic_wp and pattern[i] not in dic_pw:
                    dic_wp[word[i]] = pattern[i]
                    dic_pw[pattern[i]] = word[i]
                elif (word[i] in dic_wp and dic_wp[word[i]] != pattern[i] ) or (pattern[i] in dic_pw and dic_pw[pattern[i]] != word[i]):
                    flag = False
                    continue
            if flag:
                res.append(word)
        
        return res       
            
            
        