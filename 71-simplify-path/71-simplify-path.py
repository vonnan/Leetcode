class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        res = []
        
        for d in stack:
            if d and d != "." and d != "..":
                res.append(d)
            elif d == ".." and res:
                res.pop()
                
        return "/" + "/".join(res)
        
        