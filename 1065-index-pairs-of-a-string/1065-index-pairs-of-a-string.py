class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        
        for word in words:
            start = 0
            while word in text[start:]:
                start = text.find(word, start)
                res.append((start, start + len(word) - 1))
                start += 1
        
        return sorted(res)
                