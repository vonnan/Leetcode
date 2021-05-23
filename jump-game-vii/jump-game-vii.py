class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] !="0":
            return False
        n = len(s)
        
        dq = deque([0])
        maxPos = 0
        visited = set([0])
        
        while dq:
            start  = dq.popleft()
            if start == n-1:
                return True
            for nxt in range(max(start + minJump, maxPos +1), min(start + maxJump, n-1) +1):
                if nxt not in visited and s[nxt] == "0":
                    dq.append(nxt)
                    
            maxPos = start + maxJump
                    
            
        return False
            
            
            
            
                        
                        
                
            
            
                
            
        
                
                
                
                