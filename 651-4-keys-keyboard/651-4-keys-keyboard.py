class Solution:
    def maxA(self, n: int) -> int:
        if n <= 6:
            return n
        
        best = [0, 1]
        for i in range(2, n+1):
            curr = best[i - 1] + 1
            max_ = max(best[j] * (i - 1 - j) for j in range(i-1))
            best.append(max(curr, max_))
        
        return best[-1]
            
        
        
           