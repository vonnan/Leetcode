class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dic = {word: i for i, word in enumerate(words)}
        
        res = set([])
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                if prefix[::-1] in dic and (dic[prefix[::-1]] != i) and suffix == suffix[::-1]:
                    res.add((i, dic[prefix[::-1]]))
                    
                if suffix[::-1] in dic and (dic[suffix[::-1]] != i) and prefix == prefix[::-1]:
                    res.add((dic[suffix[::-1]], i))
        
        return res
            