class Solution:
    def maximumRemovals(self, s: str, p: str, A: List[int]) -> int:
        def check(m):
            sets = set(A[:m])
            j = 0
            
            for i, ch in enumerate(s):
                if i in sets:
                    continue
                if ch == p[j]:
                    j += 1
                    if j == len(p):
                        return True
            return False
        
        left, right = 0, len(A)
        while left < right:
            mid = (left + right + 1)//2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left