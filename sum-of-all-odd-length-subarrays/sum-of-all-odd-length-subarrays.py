class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = sum(arr)
        
        n = len(arr)
        if n <=2:
            return res
        
        size = 1
        while size <= n//2*2:
            size += 2
            for j in range(n - size + 1):
                res += sum(arr[j:j+size])
        return res
        
            
        