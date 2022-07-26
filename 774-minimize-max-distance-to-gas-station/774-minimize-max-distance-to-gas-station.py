from math import ceil
class Solution:
    def minmaxGasDist(self, A: List[int], k: int) -> float:
        left, right = 0, A[-1] - A[0]
        lst = [A[i+1] - A[i] for i in range(len(A) - 1)]
        while right - left > 10**(-6) :
            mid = (left + right)/2
            ct = 0
            for num in lst:
                if num <= mid:
                    continue
                else:
                    ct += ceil(num/mid)-1
                    if ct > k:
                        left = mid
                        break
            if ct <= k:
                right = mid
        return left
                
                
            