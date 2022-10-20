class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k > arr[-1] - len(arr):
            return k + len(arr)
        
        arr = [0] + arr
        
        for a, b in zip(arr, arr[1:]):
            gap = b - a - 1
            if gap == 0:
                continue
            elif gap <= k:
                k -= gap
                if k == 0:
                    return b - 1
            else:
                return a + k
        