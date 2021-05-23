class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != "0":
            return False
        
        queue = deque([0])
        
        n, maxPos = len(s), 0
        
        while queue:
            start = queue.popleft()
            if start == n-1:
                return True
            
            for j in range(max(start + minJump, maxPos), min(start +maxJump, n-1) +1):
                if s[j] == "0":
                    queue.append(j)
            
            maxPos = max(maxPos, start + maxJump)
                
        return False
        
            
                
            
        
                
                
                
                