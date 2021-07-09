class Solution:
    def maxProfit(self, A: List[int], orders: int) -> int:
        
        left, right, mod = 1, max(A), 10**9 + 7
        
        while left < right:
            mid = (left + right + 1)//2
            if sum(a - mid + 1 for a in A if a >= mid) < orders:
                right = mid - 1
            else:
                left = mid
                
        print(left)
        res = sum((a + left) * (a - left + 1)//2 for a in A if a >= left) % mod
        tot = sum(a - left + 1 for a in A if a >= left)
        if tot > orders:
            res -= (tot - orders) * left 
            
        return res % mod
        