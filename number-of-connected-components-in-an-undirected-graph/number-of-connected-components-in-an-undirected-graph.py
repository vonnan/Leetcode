class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        UF = {i:i for i in range(n)}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        for a, b in edges:
            UF[find(a)] = find(b)
            
        return len(set(find(i) for i in range(n)))
                
        