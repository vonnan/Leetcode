class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lst = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        dic = defaultdict(int)
        for i, word in enumerate(lst):
            for c in word:
                dic[c] = i
                
        res = []
        for word in words:
            lst = [ dic[c.lower()] for c in word]
            if len(set(lst))== 1:
                res.append(word)
        
        return res