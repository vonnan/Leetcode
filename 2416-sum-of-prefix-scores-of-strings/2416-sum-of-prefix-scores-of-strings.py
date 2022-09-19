class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        dic = defaultdict(int)
        
        for word in words:
            pre = ""
            for c in word:
                pre += c
                dic[pre] += 1
        
        res = []
        
        for word in words:
            pre = ""
            ct = 0
            for i in range(1, len(word) + 1):
                
                ct += dic[word[:i]]
            res.append(ct)
        return res
                