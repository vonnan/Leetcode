class Solution:
    def magicalString(self, n: int) -> int:
        arr, i = [1,2, 2], 2
        if n <= 3:
            return 1
        
        while i < n:
            arr.extend([3 - arr[-1] ] * arr[i])
            i += 1
        
        return arr[:n].count(1)