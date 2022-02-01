class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        n = len(s)
        def dfs(s, path):
            if sum(map(len, path)) == n:
                res.append(" ".join(path))
            
            for word in wordDict:
                m = len(word)
                if s[:m] == word:
                    dfs(s[m:], path + [word])
        
        dfs(s, [])
        return res
                
                
        