class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        A = set(wordDict)
        q, n = deque([0]), len(s)
        visited = set([0])
        while q:
            pos = q.popleft()
            for word in A:
                m = len(word)
                if pos + m <= n:
                    if s[pos:pos + m] == word:
                        if pos + m == n:
                            return True
                        if pos + m not in visited:
                            q.append(pos + m)
                            visited.add(pos+ m)
        return False
            
        