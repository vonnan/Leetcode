class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n, res = len(graph), []
        
        def dfs(curr, path):
            if curr == n-1:
                res.append(path)
            else:
                for node in graph[curr]:
                    dfs(node, path + [node])
        
        dfs(0, [0])           
        return res
            