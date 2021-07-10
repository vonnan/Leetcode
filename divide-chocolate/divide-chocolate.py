class Solution:
    def maximizeSweetness(self, A: List[int], k: int) -> int:
        k += 1
        left, right = min(A), sum(A)//k
        while left < right:
            mid = (left + right)//2
            res, ct = 0, 1
            for i, a in enumerate(A):
                if res + a > mid:
                    res = 0
                    ct += 1
                else:
                    res += a
            
            
            if ct > k:
                left = mid + 1
            else:
                right = mid
        
        return left
                
                    