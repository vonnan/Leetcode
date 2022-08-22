class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        set1 = set([(r,c) for r in range(n) for c in range(n) if img1[r][c]])
        
        def move(dr, dc):
            
            set3 = set([])
            for r,c in set1:
                if 0 <= r + dr < n and 0 <= c + dc < n:
                    set3.add((r + dr, c + dc))
            return set3
        
        set2 = set([(r,c) for r in range(n) for c in range(n) if img2[r][c]])
        
        res = 0
        for dr in range(-(n-1), n):
            for dc in range(-(n-1), n):
                set3 = move(dr, dc)
                if len(set3) <= res:
                    continue
                ct = len(set2 & set3)
                res = max(res, ct)
        
        return res