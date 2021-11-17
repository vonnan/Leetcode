class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        
        heights = [0] * col
        res = 0
        
        def maxArea(H):
            ans, n = 0, len(H)
            stack = []
            for i, h in enumerate(H):
                j = i
                while stack and stack[-1][0] > h:
                    ht, j = stack.pop()
                    ans = max(ans, ht * (i - j))
                stack.append((h, j))
            
            for h, i in stack:
                ans = max(ans, (n- i) * h)
            return ans
        
        for rows in matrix:
            for c in range(col):
                if rows[c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            res = max(res, maxArea(heights))
        
        return res
            