class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        a, b, res = 0, 0, 0
        
        for i in range(len(arr)):
            a += arr[i]
            b += sorted(arr)[i]
            res += (a== b)
        
        return res