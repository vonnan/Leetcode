class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(k):
            for i in range(k//2):
                arr[i], arr[k-1 -i] = arr[k-1-i], arr[i]
                
        res = []
        
        n = len(arr)
        
        for i in range(n -1, 0, -1):
            idx = arr.index(i + 1)
            if idx != i:
                flip(idx + 1)
                flip(i + 1)
                res.append(idx + 1)
                res.append(i + 1)
        
        return res
            