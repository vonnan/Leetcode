from bisect import bisect_left
class Solution:
    def maxDistance(self, A: List[int], m: int) -> int:
        A.sort()
        if m == 2:
            return A[-1] - A[0]
        n = len(A)
        if m == n:
            return min(A[i] - A[i-1] for i in range(1, n))
        
        left, right = 0, A[-1]
        while left < right:
            mid = (left + right + 1)//2
            start = 0
            ct = 1
            while start < n:
                idx = bisect_left(A, A[start] + mid, start)
                if idx == start or idx == n:
                    break
                start = idx
                ct += 1
                if ct >= m:
                    break
            #print(mid, ct)
            if ct >= m:
                left = mid
            else:
                right = mid - 1
        return left
            
        
        