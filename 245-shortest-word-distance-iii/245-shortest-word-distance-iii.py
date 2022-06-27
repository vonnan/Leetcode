from bisect import bisect
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dic = defaultdict(list)
        for i, word in enumerate(wordsDict):
            dic[word].append(i)
        
        lst1, lst2 = dic[word1], dic[word2]
        if word1 == word2:
            return min(lst1[i+1]-lst1[i] for i in range(len(lst1)-1))
        else:
            res = inf
            lst2 = [-inf] + lst2 + [inf]
            for i in lst1:
                idx = bisect(lst2, i)
                res = min(res, min(lst2[idx] - i, i - lst2[idx - 1]))
        
        return res
                
                