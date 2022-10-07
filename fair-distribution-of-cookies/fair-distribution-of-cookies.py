class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dp = [0] * k
        n = len(cookies)
        if n == k:
            return max(cookies)
        
        self.res = sum(cookies)
        
        def dfs(pos, path):
            if pos == n:
                self.res = min(self.res, max(path))
                return
            
            for i in range(k):
                dfs(pos + 1, path[:i] + [path[i] + cookies[pos]] + path[i+1:])
        
        dfs(0, dp)
        
        return self.res
        
