class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        
        def dfs(s, seen):
            if not s:
                return 0
            
            res = 0
            
            for i in range(1, len(s) +1):
                candidate = s[:i]
                if candidate not in seen and len(s) -i  >= res:
                    seen.add(candidate)
                    res = max(res, 1 + dfs(s[i:], seen))
                    seen.remove(candidate)
            return res
        
        return dfs(s, seen)