class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}
        if not digits:
            return []
        
        res = set([""])
        for d in digits:
            res = set([x + c for c in dic[d] for x in res])
        
        return res