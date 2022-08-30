class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        graph = defaultdict(set)
        
        for rt, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(rt)
        
        q = deque([source])
        
        res = 1
        
        visited_rt, visited_stop = set([]), set([])
        
        while q:
            m = len(q)
            for _ in range(m):
                stop = q.popleft()
                for rt in graph[stop]:
                    if rt not in visited_rt:
                        visited_rt.add(rt)
                        for stop in routes[rt]:
                            if stop == target:
                                return res
                            elif stop not in visited_stop:
                                visited_stop.add(stop)
                                q.append(stop)
            res += 1
        
        return -1
                
            