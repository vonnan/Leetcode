class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dic = {w[::-1]:i for i, w in enumerate(words)}
        res = set([])
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                if prefix in dic and suffix == suffix[::-1] and dic[prefix] != i:
                    res.add((i, dic[prefix]))
                if suffix in dic and prefix == prefix[::-1] and dic[suffix] != i:
                    res.add((dic[suffix], i))
        return res
                