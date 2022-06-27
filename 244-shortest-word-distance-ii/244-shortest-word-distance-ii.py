from bisect import bisect
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dic = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.dic[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        lst1, lst2 = [-inf] + self.dic[word1] + [inf], [-inf] + self.dic[word2] + [inf]
        res = inf
        for i in lst1[1:-1]:
            idx = bisect(lst2, i)
            res = min(res, min(i -lst2[idx-1], lst2[idx] - i))
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)