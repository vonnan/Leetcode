class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrom(x):
            return x == x[::-1]
        
        res = []
        
        def dfs(x, path):
            if not x:
                if path:
                    res.append(list(path))
                return
            
            for i in range(1, len(x) + 1):
                prefix = x[:i]
                if isPalindrom(prefix):
                    path.append(prefix)
                    dfs(x[i:], path)
                    path.pop()
        
        dfs(s, [])
        return res