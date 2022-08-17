from bisect import bisect
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if citations[-1] < 1:
            return 0
        
        left, right = 0, n -1
        while left < right:
            mid = (left + right)//2
            if citations[mid] >=  n - mid:
                right = mid
            else:
                left = mid + 1
        return n - left
