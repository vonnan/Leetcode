class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        
        else:
            return [x + [tail] for tail in range(n, k-1, -1) for x in self.combine(tail-1, k-1)]