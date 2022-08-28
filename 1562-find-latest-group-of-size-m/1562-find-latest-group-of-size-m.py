from bisect import insort

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        n = len(arr)
        if m == n:
            return n
        
        lst = [0] * (n + 2)
        res = -1
        for i, a in enumerate(arr):
            left, right = lst[a - 1], lst[a + 1]
            if left == m or right == m:
                res = i
            
            lst[a-left] = lst[a + right] = left + right + 1
        
        return res
        
        
            