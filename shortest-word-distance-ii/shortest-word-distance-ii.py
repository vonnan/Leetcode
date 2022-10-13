from bisect import bisect

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dic = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.dic[word].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        lst1, lst2 = self.dic[word1], self.dic[word2]
        if len(lst2) > len(lst1):
            lst1, lst2 = lst2, lst1
        res = inf
        lst1 = [-inf] + lst1 + [inf]
        for num in lst2:
            idx = bisect(lst1, num)
            res = min(res, min(num - lst1[idx - 1], lst1[idx] - num))
        return res
            
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)