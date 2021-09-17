class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = [""]* len(queries)
        visited = set([])
        sets = set(wordlist)
        for i, q in enumerate(queries):
            if q in sets:
                res[i] = q
                visited.add(i)
        dic2, dic = {}, {}
        for word in wordlist:
            if word.upper() not in dic2:
                dic2[word.upper()] = word
            wd = "".join([c if c not in "aeiou" else "*" for c in word.lower()])
            if wd not in dic:
                dic[wd] = word
          
        for i, q in enumerate(queries):
            if i not in visited:
                if q.upper() in dic2:
                    res[i] = dic2[q.upper()]
                else:
                    q =  "".join([c if c not in "aeiou" else "*" for c in q.lower()])
                    if q in dic:
                        res[i] = dic[q]
       
        return res
                
                    
                
                        
               
                
        