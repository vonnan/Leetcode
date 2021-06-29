class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        row, col, res = len(matrix), len(matrix[0]), 0
        heights = [0] * col
        
        def maxArea(height):
            maxArea, n = 0, len(height)
            stack = []
            for i, h in enumerate(height):
                j = i
                while stack and stack[-1][0] > h:
                    ht, j = stack.pop()
                    maxArea = max(maxArea, ht * (i - j))
                stack.append((h, j))
            for h, i in stack:
                maxArea = max(maxArea, h * (n- i))
            return maxArea
            
        for rows in matrix:
            for i in range(col):
                if rows[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            res = max(res, maxArea(heights))
            
        return res
            
        
            