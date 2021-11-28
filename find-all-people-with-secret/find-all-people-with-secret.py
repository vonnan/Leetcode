class Solution:
    def findAllPeople(self, n: int, A: List[List[int]], first: int) -> List[int]:
        res = set([0, first])
        time = defaultdict(dict)
        A.sort(key = lambda x: x[2])
        sets = defaultdict(set)
        
                        
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        for u, v, t in A:
            if u not in time[t]:
                time[t][u] = set([v])
            else:
                time[t][u].add(v)
                
            if v not in time[t]:
                time[t][v] = set([u])
            else:
                time[t][v].add(u)
                
            sets[t].add(u)
            sets[t].add(v)
        
        for t in sorted(time.keys()):
            q = deque(list(res & sets[t]))
            dic = time[t]
            while q:
                u = q.popleft()
                for v in dic[u]:
                    if v not in res:
                        res.add(v)
                        q.append(v)
        
        return res
            
            

            
        return res
                