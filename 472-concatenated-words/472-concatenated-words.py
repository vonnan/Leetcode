class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dic = defaultdict(list)
        
        for word in words:
            dic[word[0]].append(word)
            
        for c in dic:
            dic[c].sort(key = len, reverse = 1)
            
        def check(word, pos, seen):
            if pos == len(word):
                if len(seen) > 1:
                    return True
                else:
                    return False
            
            c = word[pos]
            for wd in dic[c]:
                m = len(wd)
                if pos + m not in seen and word[pos:pos + m] == wd:
                    if check(word, pos + m, seen | set([pos + m])):
                        return True
            return False
        
        res = []
        for word in words:
            seen = set([])
            if check(word, 0, seen):
                res.append(word)
                
        return res
                