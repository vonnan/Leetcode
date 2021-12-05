class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]
        for h in height:
            left.append(max(h, left[-1]))
        
        right = [0]
        for h in height[::-1]:
            right.append(max(h, right[-1]))
            
        left, right = left[1:], right[1:][::-1]
        res = 0
        for i, h in enumerate(height):
            l,r = left[i], right[i]
            bar = min(l,r)
            if h < bar:
                res += (bar - h)
        return res
            