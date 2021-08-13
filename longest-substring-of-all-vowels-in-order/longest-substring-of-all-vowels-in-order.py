class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        if n < 5 or len(set(word)) < 5:
            return 0
        
        res, lst = 0, [word[0]]
        for i, s, in enumerate(word[1:], 1):
            if s >= lst[-1]:
                lst.append(s)
            else:
                if len(set(lst)) ==5:
                    res = max(res, len(lst))
                lst = [s]
        
        if len(set(lst)) ==5:
            res = max(res, len(lst))
        
        return res
                
                    