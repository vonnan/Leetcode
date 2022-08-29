class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nei = defaultdict(set)
        
        for u, v in edges:
            nei[u].add(v)
            nei[v].add(u)
            
        MHT = set(range(n))
        
        while len(MHT) > 2:
            leaves = set([u for u in MHT if len(nei[u]) == 1])
            MHT -= leaves
            for u in leaves:
                for v in nei[u]:
                    nei[v].remove(u)
        
        return MHT