class Solution:
    def maximizeSweetness(self, A: List[int], k: int) -> int:
        left, right = min(A), sum(A)//(k + 1)
        while left < right:
            mid = (left + right)//2
            ct, tot = 1, 0
            for a in A:
                if tot + a <= mid:
                    tot += a
                else:
                    ct += 1
                    tot = 0
                    if ct > k + 1:
                        left = mid + 1
                        break
            if ct <= k + 1:
                right = mid
        return left
        
        