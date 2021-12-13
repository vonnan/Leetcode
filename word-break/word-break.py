class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        A= set(wordDict)
        q = deque([0])
        n = len(s)
        
        visited = set([])
        
        while q:
            pos = q.popleft()
            if pos == n:
                return True
            for word in A:
                m = len(word)
                if s[pos: pos + m] == word:
                    if pos + m == n:
                        return True
                    if pos + m not in visited:
                        visited.add(pos + m)
                        q.append(pos + m)
        return False