class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        nei = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                nei[stop].add(i)
                
        q = deque([source])
        visited_rt, visited_stop = set([]), set([source])
        
        res = 0
        while q:
            m = len(q)
            for _ in range(m):
                stop = q.popleft()
                if stop == target:
                    return res
                for rt in nei[stop]:
                    if rt not in visited_rt:
                        visited_rt.add(rt)
                        for stop in routes[rt]:
                            if stop not in visited_stop:
                                q.append(stop)
                                visited_stop.add(stop)
            res += 1
        
        return -1
        