class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse = True)
        
        if sum(arr) <= target:
            return arr[0]
        
        while arr and target > arr[-1] * len(arr):
            target -= arr.pop()
        
        return int(round((target -0.00001)/len(arr)))