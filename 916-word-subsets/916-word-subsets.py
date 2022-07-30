class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        res = []
        counter = Counter([])
        for word in words2:
            counter |= Counter(word)
        
        return [word for word in words1 if Counter(word) & counter == counter]
        