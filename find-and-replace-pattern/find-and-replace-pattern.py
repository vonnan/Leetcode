class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        n = len(pattern)
        
        res = []
        
        for word in words:
            if len(word) != n:
                continue
            dic_wp, dic_pw = {}, {}
            
            flag = True    
            for i in range(n):
                w, p = word[i], pattern[i]
                
                if (w not in dic_wp) and (p not in dic_pw):
                    dic_wp[w] = p
                    dic_pw[p] = w
                    
                elif (w in dic_wp and dic_wp[w] != p) or (p in dic_pw and dic_pw[p] != w):
                    flag = False
                    break
                
            if flag:    
                res.append(word)
                
        return res
        