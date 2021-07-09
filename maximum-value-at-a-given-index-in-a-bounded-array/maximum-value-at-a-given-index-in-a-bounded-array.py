class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        
        def check(m):
            l = max(0, m - index)
            res = (l + m) *(m - l + 1)//2
            r = max(0, m - (n-1-index))
            res += (r + m) * (m - r + 1)//2
            return (res - m) <= maxSum
        
        
        left, right = 0, maxSum
        
        while left < right:
            mid = (left + right + 1)//2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        
        return left + 1 
            