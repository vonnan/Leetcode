class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        dic_r = {i: word for i, word in enumerate(words)}
        dic_c = {i:"" for i in range(n)}
        
        for r, word in enumerate(words):
            if len(word) > n:
                return False
            
            for c, s in enumerate(word):
                dic_c[c] += s
            
        for r in range(n):
            if dic_r[r] != dic_c[r]:
                return False
        
        return True