class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        t3 = [[] for _ in range(n)]
        gr = [[] for _ in range(n)]

        for a, b in edges:
            gr[a].append(b)
            gr[b].append(a)

        for v in range(n):
            for to in gr[v]:
                t3[v].append((scores[to], to))
            t3[v] = sorted(t3[v], reverse=True)[:3]

        mx = -1
        for a, b in edges:
            for sa, ta in t3[a]:
                if ta == b: continue
                for sb, tb, in t3[b]:
                    if tb == a or tb == ta: continue
                    mx = max(mx, sa + sb + scores[a] + scores[b])

        return mx                
            
        
        