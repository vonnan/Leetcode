class Solution:
    def sequenceReconstruction(self, nums: List[int], As: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        
        for A in As:
            m = len(A)
            for i, a in enumerate(A):
                if i != len(A)-1:
                    graph[a].append(A[i+1])
                if i:
                    indegree[a] += 1
                else:
                    indegree[a] += 0
        
        stack = [key for key, val in indegree.items() if not val]
        
        res = []
        
        while stack:
            if len(stack) != 1:
                return False
            u = stack.pop()
            res.append(u)
            
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    stack.append(v)
        
        return len(res) == len(graph) and res == nums
                    
                    
                    
        
              
        
        
        