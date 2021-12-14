class Solution:
    def possibleBipartition(self, n: int, A: List[List[int]]) -> bool:
        m = len(A)
        if not A or m <= 1:
            return True
        dic= defaultdict(set)
        
        for a, b in A:
            dic[a].add(b)
            dic[b].add(a)
            
        color = { i: None for i in range(1, n+1)}
    
        def dfs(node, c):
            if not color[node]:
                color[node] = c
            else:
                return color[node] == c
            
            for enemy in dic[node]:
                if not dfs(enemy, 1-c):
                    return False
            return True
        
        for i in range(1, n+ 1):
            if not color[i] and not dfs(i, 0):
                return False
        return True
            