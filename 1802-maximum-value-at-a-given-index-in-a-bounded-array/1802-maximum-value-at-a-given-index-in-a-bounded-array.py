class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        res = 1
        maxSum -= n
        left, right = index, index + 1
        while maxSum >= right - left:
            
            res += 1
            maxSum -= right - left
                
            if left > 0:
                left -= 1
            if right < n:
                right += 1
                
            if left == 0 and right == n:
                return res + maxSum//n
            
        
        return res
            
            