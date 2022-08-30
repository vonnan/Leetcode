class Solution:
    def ladderLength(self, s: str, e: str, wordList: List[str]) -> int:
        nei = defaultdict(set)
        
        if e not in wordList:
            return 0
        n = len(s)
        wordList += [s]
        
        for word in wordList:
            for i in range(n):
                new = word[:i] + "*" + word[i+1:]
                nei[new].add(word)
        
        res = 0
        q = deque([e])
        visited = set([e])
        
        while q:
            res += 1
            m = len(q)
            for _ in range(m):
                word = q.popleft()
                if word == s:
                    return res
                for i in range(n):
                    new = word[:i] + "*" + word[i+ 1:]
                    for nxt in nei[new]:
                        if nxt not in visited:
                            q.append(nxt)
                            visited.add(nxt)
        return 0
                            
        
        