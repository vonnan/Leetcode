class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse = 1)
        maxA, n = arr[0], len(arr)
        while arr and arr[-1] * n < target:
            target -= arr.pop()
            n -= 1
        return int(round((target -0.0001)/n)) if n else maxA
        
        
        
       
            
                    
        