class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(heights[0], 0)]
        res = max(heights)
        
        for i, h in enumerate(heights[1:], 1):
            j = i
            while stack and h <= stack[-1][0]:
                hj, j = stack.pop()
                res = max(res, hj * (i - j))
            stack.append((h, j))
        
        n = len(heights)
        for h, idx in stack:
            res = max(res, (n - idx) * h)
        
        return res