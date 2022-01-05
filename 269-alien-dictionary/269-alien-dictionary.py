class Solution:
    def alienOrder(self, words: List[str]) -> str:
        nei = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}
        
        for first, second in zip(words, words[1:]):
            n1, n2 = len(first), len(second)
            if n1 > n2 and first[:n2] == second:
                return ""
            for a, b in zip(first, second):
                if a != b:
               
                    if b not in nei[a]:
                        nei[a].add(b)
                        indegree[b] += 1
                    break
                 
        q = deque([c for c, val in indegree.items() if val == 0])
        res = ""
        
        while q:
            c = q.popleft()
            res += c
            
            for a in nei[c]:
                
                indegree[a] -= 1
                
                if indegree[a] == 0:
                    q.append(a)
                    
       
        return res if len(res) == len(indegree) else ""
            