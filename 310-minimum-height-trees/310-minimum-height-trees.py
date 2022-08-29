class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nei = defaultdict(set)
        
        for u, v in edges:
            nei[u].add(v)
            nei[v].add(u)
            
        MHT = set(range(n))
        leaves = set([u for u in MHT if len(nei[u])== 1])
        
        while len(MHT) > 2:
            MHT -= leaves
            new = set([])
            for u in leaves:
                for v in nei[u]:
                    nei[v].remove(u)
                    if v in MHT and len(nei[v]) == 1:
                        new.add(v)
            leaves = new
                    
        return MHT
                