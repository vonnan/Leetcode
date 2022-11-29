from sortedcontainers import SortedList

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
            
        res = [-1] * n
        
        @lru_cache(None)
        def dfs(i):
            if res[i] > 0:
                return res
            
            res[i] = i
            
            for j in graph[i]:
                if quiet[res[i]] > quiet[dfs(j)]:
                    res[i] = res[j]
            
            return res[i]
        
        for i in range(n):
            dfs(i)
            
        return res
            
        
      
        
        
            
            
            