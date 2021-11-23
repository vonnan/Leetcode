class Solution:
    def alienOrder(self, words: List[str]) -> str:
        nei = defaultdict(set)
        degree = {c: 0 for word in words for c in word}
        for first, second in zip(words, words[1:]):
            n1, n2 = len(first), len(second)
            if n2 < n1 and second == first[:n2]:
                return ""
            for a,b in zip(first, second):
                if a != b:
                    if b not in nei[a]:
                        nei[a].add(b)
                        degree[b] += 1
                    break
        
        res = ""
        q = deque([c for c in degree if degree[c] == 0])
        
        while q:
            c = q.popleft()
            res += c
            for d in nei[c]:
                degree[d] -= 1
                if degree[d] == 0:
                    q.append(d)
                    
        if len(res) == len(degree):
            return res
        else:
            return ""
            
            
                