class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        res = 0
        nei = defaultdict(list)
        
        for u, v in edges:
            nei[u].append((scores[v], v))
            nei[v].append((scores[u], u))
            
        for u in nei:
            nei[u] =sorted(nei[u])[-3:]
            
        for a, b in edges:
            ct = scores[a] + scores[b]
            for su, u in nei[a]:
                if u == b:
                    continue
                else:
                    for sv, v in nei[b]:
                        if v== a or v == u:
                            continue
                        else:
                            res = max(res, ct + su + sv)
        
        return res if res else -1
                
            
                
            
        
        