class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([0])
        
        dic = defaultdict(set)
        for word in wordDict:
            dic[word[0]].add(word)
        
        seen = set([0])
        n = len(s)
        
        while q:
            pos = q.popleft()
            if pos == n:
                return True
            
            for word in dic[s[pos]]:
                np = pos + len(word)
                if np not in seen and s[pos:np] == word:
                    q.append(np)
                    seen.add(np)
            
        return False
            
        
        
        