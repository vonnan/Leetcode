class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        
        def dfs(x, path):
            if not x:
                if path:
                    print(path)
                    res.append(tuple(path))
            
            else:
                for i in range(1, len(x) + 1):
                    prefix = x[:i]
                    
                    if prefix == prefix[::-1]:
                        path.append(prefix)
                        dfs(x[i:], path)
                        path.pop()
        
        dfs(s, [])
        return res