class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        
        visited = set()
        next_jump = set()
        
        if arr[start]+start <n:
            next_jump.add(arr[start]+start)
        if start - arr[start] >=0:
            next_jump.add(start - arr[start])
        
        while len(next_jump) > 0:
            next_next_jump = set()
            for start in next_jump:
                if arr[start] ==0:
                    return True
                if start not in visited:
                    right, left = arr[start]+start, start - arr[start] 
                    if  right<n:
                        if arr[right] ==0:
                            return True
                        next_next_jump.add(right)
                        
                        
                    if left >=0:
                        if arr[left] ==0:
                            return True
                        next_next_jump.add(left)
                    
                    visited.add(start)
                    
                
            next_jump = next_next_jump
            
        if len(next_jump) ==0:
            return False
            
            
        