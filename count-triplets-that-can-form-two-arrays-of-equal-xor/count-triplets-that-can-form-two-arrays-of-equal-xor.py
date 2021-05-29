class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        arr = [0] + arr
        n, res = len(arr), 0
        for i in range(1, n):
            arr[i] ^= arr[i-1] 
        
        
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] == arr[j]:
                    res += j - i - 1
                    
        return res
        