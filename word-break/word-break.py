class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        A = set(wordDict)
        visited = set([])
        q, n = deque([0]), len(s)
        
        while q:
            idx = q.popleft()
            for word in A:
                w = len(word)
                if s[idx: idx + w] == word:
                    if idx + w == n:
                        return True
                    if idx + w not in visited:
                        q.append(idx + w)
                        visited.add(idx + w)
        return False
                    