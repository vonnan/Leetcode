
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
            
        for u in graph:
            graph[u].sort(reverse = True)
            
        def dfs(src):
            dst = graph[src]
            while dst:
                nxt = dst.pop()
                dfs(nxt)
            res.append(src)
        
        dfs("JFK")
        return res[::-1]
            