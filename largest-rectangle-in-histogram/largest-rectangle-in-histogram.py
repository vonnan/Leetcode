class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack, max_area = [], 0
        
        for i, h in enumerate(heights):
            j = i
            while stack and stack[-1][1] > h:
                j, ht = stack.pop()
                max_area = max(max_area, ht* (i - j))
            stack.append((j, h))
        print(stack)
        for i, h in stack:
            max_area = max(max_area, h * (n - i))
            
        return max_area