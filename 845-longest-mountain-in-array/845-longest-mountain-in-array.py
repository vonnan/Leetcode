class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        arr = [inf] + arr + [inf]
        start, rise_flag = 0, True
        dp_up = [0] * len(arr)
        for i in range(1, len(arr)- 1):
            if arr[i] > arr[i-1]:
                dp_up[i] = dp_up[i-1] + 1
        
        dp_down = [0]* len(arr)
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                dp_down[i] = dp_down[i+1] + 1
        
        
        
        lst = [a + b + 1 for a, b in zip(dp_up, dp_down) if a and b]
        if not lst:
            return 0
        return max(lst)
    
                
                
                    