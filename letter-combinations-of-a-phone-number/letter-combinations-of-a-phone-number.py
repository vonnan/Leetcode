class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}
        if not digits:
            return []
        
        res = set([""])
        
        for c in digits:
            new = set([])
            for nxt in dic[c]:
                new |= set([word + nxt for word in res] )
            res = new
        return res