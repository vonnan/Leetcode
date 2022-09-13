class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dp = [0] * k
        self.res = sum(cookies)
        n = len(cookies)
        if n <= k:
            return max(cookies)
           
        def dfs(path, pos):
            if pos == n:
                self.res = min(self.res, max(path))
                return
                
            for i in range(k):
                nxt = path[:i] + [path[i] + cookies[pos]] + path[i+1:]
                #print(i, nxt)
                dfs(nxt, pos + 1)
        
        dfs(dp, 0)
        
        return self.res
        
