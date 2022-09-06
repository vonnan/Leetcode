class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if len(original) != m * n:
            return []
        
        for r in range(m):
            
            res.append(original[r * n : (r + 1) * n])
            
        return res