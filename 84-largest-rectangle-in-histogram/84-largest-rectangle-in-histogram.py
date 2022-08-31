class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_ = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                H, start = stack.pop()
                max_ = max(max_, H * (i - start))
            stack.append((h, start))
        n = len(heights)
        while stack:
            H, start = stack.pop()
            max_ = max(max_, (n - start) * H)
        
        return max_