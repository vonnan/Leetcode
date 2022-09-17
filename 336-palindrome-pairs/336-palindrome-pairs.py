class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dic = {word[::-1]: i for i, word in enumerate(words)}
        
        res = set([])
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                if prefix in dic and (dic[prefix] != i) and suffix == suffix[::-1]:
                    res.add((i, dic[prefix]))
                    
                if suffix in dic and (dic[suffix] != i) and prefix == prefix[::-1]:
                    res.add((dic[suffix], i))
        
        return res
            