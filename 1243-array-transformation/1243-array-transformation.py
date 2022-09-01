class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        while True:
            new = arr[:]
            for i in range(1, n-1):
                if new[i] < arr[i+1] and new[i] < arr[i -1]:
                    new[i] += 1
                elif new[i] > arr[i+1] and new[i] > arr[i-1]:
                    new[i] -= 1
            if arr == new:
                return arr
            arr = new
            
            