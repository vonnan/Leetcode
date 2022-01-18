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
                    
        q, seen = deque([(s1, 0)]), set([A])
        
        while q:
            x, d = q.popleft()
            if x== s2:
                return d
            for y in nei(x):
                if y not in seen:
                    seen.add(y)
                    q.append((y, d + 1))
        