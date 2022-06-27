class Solution:
    
    def generateAbbreviations(self, word: str) -> List[str]:
        
        res = []
        
        def dfs(word, tmp):
            if not word:
                res.append(tmp)
                
            for i, w in enumerate(word):
                if not tmp or tmp[-1].isdigit():
                    dfs(word[i+1:], tmp + word[:i+1])
                if not tmp or tmp[-1].isalpha():
                    dfs(word[i+1:], tmp + str(i+1))
                    
        
        dfs(word, "")
        return res
            
                
            
            
        