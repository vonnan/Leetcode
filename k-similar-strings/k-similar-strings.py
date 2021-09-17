class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        n = len(s1)
        def nei(s):
            i = 0
            while s[i] == s2[i]:
                i += 1
            for j in range(i+1,n):
                if s[j] == s2[i]:
                    yield s[:i] + s[j] + s[i+1:j] + s[i]+ s[j+1:]
        
        q, res = deque([s1]), 0
        visited = set([s1])
        while q:
            m = len(q)
            for _ in range(m):
                s = q.popleft()
                if s== s2:
                    return res
                
                for x in nei(s):
                    if x not in visited:
                        visited.add(x)
                        q.append(x)
                        if x==  s2:
                            return res + 1
            res += 1
                
        
        
        
        
                
                    
            