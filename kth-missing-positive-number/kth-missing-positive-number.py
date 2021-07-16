class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k > arr[-1] - len(arr):
            return k + len(arr)
        
        else:
            for i in range(1, arr[-1]):
                if arr[0] == i:
                    arr.pop(0)
                else:
                    k -= 1
                    if k == 0:
                        return i