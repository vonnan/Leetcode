class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        arr = [0] + arr
        
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        
        res = 0
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[j]== arr[i]:
                    res += j - i - 1
        return res
