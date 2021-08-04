class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        dic = {}
        def dfs(pattern, s):
            if not pattern:
                if s:
                    return False
                else:
                    return True
                
            for end in range(1, len(s) - len(pattern) + 2):
                if pattern[0] not in dic and s[:end] not in dic.values():
                    dic[pattern[0]] = s[:end]
                    if dfs(pattern[1:], s[end:]):
                        return True
                    del dic[pattern[0]]
                    
                elif pattern[0] in dic and dic[pattern[0]]== s[:end]:
                    if dfs(pattern[1:], s[end:]):
                        return True
                    
            return False
        
        return dfs(pattern, s)