class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if not s or not wordDict:
            return 
        
        words, n = set(wordDict), len(s)
        
        visited = set([])
        
        q = deque([0])
        
        while q:
            m = len(q)
            for _ in range(m):
                i = q.popleft()
                for j in range(i + 1, n +1):
                    for word in words:
                        if s[i:j] == word:
                            if j == n:
                                return True
                            
                            if j not in visited:
                                visited.add(j)
                                q.append(j)
            
                                
        
        
            
        
                        
                
                
                    
                    