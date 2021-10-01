class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":"abc", "3": "def", "4": "ghi", "5": "jkl", "6" : "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        if not digits:
            return []
        
        sets = set([""])
        
        for num in digits:
            sets = set([path + c for path in sets for c in dic[num]])
            
        return sets