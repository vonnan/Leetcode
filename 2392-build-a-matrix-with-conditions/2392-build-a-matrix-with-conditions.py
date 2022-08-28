class Solution:
    def buildMatrix(self, k: int, row: List[List[int]], col: List[List[int]]) -> List[List[int]]:
        def dfs(A):
            indegree = defaultdict(int)
            graph = defaultdict(set)
            q = deque([])
            A = set([tuple(a) for a in A])
            for u, v in A:
                indegree[v] += 1
                graph[u].add(v)
            
            ans = []
            seen = set([])
            for u in range(1, k + 1):
                if indegree[u] == 0:
                    q.append(u)
                    seen.add(u)
            
            while q:
                u = q.popleft()
                ans.append(u)
                seen.add(u)
                for v in graph[u]:
                    indegree[v] -= 1
                    
                    if indegree[v] == 0:
                        if v not in seen:
                            q.append(v)
            
            return ans if len(seen) == k else []
        
        res_r, res_c = dfs(row), dfs(col)
        print(res_r, res_c)
        
        if not res_r or not res_c:
            return []
        
        res = [[0] * k for _ in range(k)]
        print(res)
        for u in range(1, k + 1):
            
            res[res_r.index(u)][res_c.index(u)] = u
        
        return res
        
                                       
                        
                        
            
            
            