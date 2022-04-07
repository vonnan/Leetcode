class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def perm(s, path, m, res):
            if len(path) == m:
                res.append(tuple(path))
                
            for i in range(len(s)):
                if i > 0 and s[i] == s[i-1]:
                    continue
                perm(s[:i] + s[i+1:], path + [s[i]], m, res)
            
            return res
                
            
        
        n = len(tiles)
        res = set([])
        for i in range(1, n+1):
            for x in perm(tiles, [], i, []):
                res.add("".join(x))
        return len(res)
            
        