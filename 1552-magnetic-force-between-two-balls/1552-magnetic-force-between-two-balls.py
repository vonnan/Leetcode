from bisect import bisect_left
class Solution:
    def maxDistance(self, A: List[int], m: int) -> int:
        A.sort()
        if m == 2:
            return A[-1] - A[0]
        n = len(A)
        if m == n:
            return min(A[i] - A[i-1] for i in range(1, n))
        print(A)
        left, right = 0, A[-1]
        while left < right:
            mid = (left + right + 1)//2
            start = A[0]
            ct = 1
            for num in A[1:]:
                if num - start >= mid:
                    ct += 1
                    if ct > m or A[-1] - num < mid:
                        break
                    start = num
            #print(mid, ct, left, right)
            if ct >= m:
                left = mid
            else:
                right = mid - 1
                
        return left
            
        
        