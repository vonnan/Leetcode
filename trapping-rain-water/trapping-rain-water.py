class Solution:
    def trap(self, A: List[int]) -> int:
        left= [0]
        for h in A:
            left.append(max(h, left[-1]))
        
        right = [0]
        for h in A[::-1]:
            right.append(max(h, right[-1]))
        
        right = right[::-1]
        res = 0
        
        for i, h in enumerate(A):
            bar = min(left[i], right[i])
            if bar > h:
                res += bar - h
        return res
        