class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0] * n, [0]* n
        
        for i in range(1, n):
            left[i] = max(left[i-1], height[i-1])
        
        for j in range(n-2, -1, -1):
            right[j] = max(right[j+1], height[j+1])
        
        res = 0
        for i in range(n):
            bar = min(left[i], right[i])
            if bar > height[i]:
                res += bar - height[i]
        
        return res