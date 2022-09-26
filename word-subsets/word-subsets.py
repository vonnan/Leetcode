class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ct2 = Counter([])
        for word in words2:
            ct2 |= Counter(word)
        
        res = []
        
        for word in words1:
            if ct2 & Counter(word) == ct2:
                res.append(word)
        
        return res