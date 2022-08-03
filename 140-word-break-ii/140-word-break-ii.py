class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        
        def dfs(s, path):
            if not s:
                res.append(" ".join(path))
            
            for word in wordDict:
                m = len(word)
                if s[:m] == word:
                    dfs(s[m:], path + [s[:m]])
        
        dfs(s, [])
        return res