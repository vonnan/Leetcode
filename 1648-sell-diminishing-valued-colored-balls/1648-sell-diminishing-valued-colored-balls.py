class Solution:
    def maxProfit(self, A: List[int], orders: int) -> int:
        left, right = 1, max(A)
        while left < right:
            mid = (left + right + 1)//2
            tot = sum([a - mid + 1 for a in A if a >= mid])
            if tot >= orders:
                left = mid
            else:
                right = mid - 1
        
        mod = 10 **9 + 7
        tot = sum([a -left + 1 for a in A if a >= left])
        print(left, tot)
        res = sum((a + left) * (a - left + 1)//2 for a in A if a >= left)
        if tot == orders:
            return res % mod
        else:
            return (res - left * (tot - orders)) % mod
            