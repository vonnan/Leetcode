class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
        n = len(A)
        stack = []
        max_ = 0
        for i, h in enumerate(A):
            start = i
            while stack and stack[-1][0] > h:
                H, start = stack.pop()
                max_ = max(max_, H * (i - start))
            stack.append((h, start))
            
        while stack:
            H, start = stack.pop()
            max_ = max(max_, (n - start) * H)
        
        return max_
            