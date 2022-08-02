class Solution:
    def lastRemaining(self, n: int) -> int:
        def helper(n, isleft):
            if n == 1:
                return 1
            
            if isleft:
                return 2 * helper(n//2, 0)
            
            elif n%2:
                return 2* helper(n//2, 1)
            
            else:
                return 2 * helper(n//2, 1) - 1
            
        return helper(n, 1)
            
        
            
            