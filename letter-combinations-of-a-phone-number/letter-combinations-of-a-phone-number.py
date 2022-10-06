class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}
        if not digits:
            return []
        
        res = set([])
        n = len(digits)
        def dfs(word, path):
            if not word and len(path) == n:
                res.add(path)
            
            for i, s in enumerate(word):
                for c in dic[s]:
                    
                    dfs(word[i+1:], path + c)
        
        dfs(digits, "")
        return res