class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic= {"2": "abc", "3": "def", "4":"ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        res = []
        if not digits:
            return res
        
        def dfs(idx, path):
            if idx == len(digits):
                res.append(path)
                return 
               
            for char in dic[digits[idx]]:
                dfs(idx + 1, path + char)
                
        dfs(0, "")
        
        return res
            
                