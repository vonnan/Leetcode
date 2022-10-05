class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        
        if end not in bank:
            return -1
        
        bank = [start] + list(set(bank))
        
        graph = defaultdict(set)
        seen = set([start])
        
        n = len(bank)
        for i, word in enumerate(bank):
            for j, wj in enumerate(bank[i+1:], i + 1):
                for k in range(8):
                    if word[:k] + word[k+1:] == wj[:k] + wj[k+1:]:
                        graph[word].add(wj)
                        graph[wj].add(word)
                        break
        
        q = deque([start])
        res = 0
        while q:
            res += 1
            m = len(q)
            for _ in range(m):
                word = q.popleft()
                for wj in graph[word]:
                    if wj == end:
                        return res
                    
                    if wj not in seen:
                        seen.add(wj)
                        q.append(wj)
        
        return -1
        