class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        
        def nei(x):
            i = 0
            while x[i] == s2[i]:
                i += 1
            
            for j in range(i+1, len(x)):
                if x[j] == s2[i]:
                    yield x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:]
                    
        q, seen, res = deque([s1]), set([A]), 0
        
        while q:
            m = len(q)
            for _ in range(m):
                x = q.popleft()
                for y in nei(x):
                    if y == s2:
                        return res + 1
                    if y not in seen:
                        seen.add(y)
                        q.append(y)
            res += 1
        