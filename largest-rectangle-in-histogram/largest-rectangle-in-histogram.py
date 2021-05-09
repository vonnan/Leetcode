class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        
        for i, h in enumerate(heights):
            j = i
            while stack and stack[-1][1] > h:
                j, p = stack.pop()
                max_area = max(max_area, (i-j)*p)
            stack.append([j,h])
                
        while stack:
            i, h = stack.pop()
            max_area = max(max_area, (len(heights) - i)*h)
            
        return max_area
        
        