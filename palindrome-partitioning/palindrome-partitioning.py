class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrom(s):
            return s == s[::-1]
        
        res = []
        
        def dfs(sub, path):
            if not sub:
                if path:
                    res.append(list(path))
                return
            
            for i in range(1, len(sub) +1):
                prefix = sub[:i]
                if isPalindrom(prefix):
                    path.append(prefix)
                    dfs(sub[i:], path)
                    path.pop()
        dfs(s, [])
        return res
                