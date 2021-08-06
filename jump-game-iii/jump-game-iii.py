class Solution:
    def canReach(self, A: List[int], start: int) -> bool:
        if 0 <= start < len(A) and A[start] >= 0:
            A[start] = - A[start]
            return A[start] == 0 or self.canReach(A, start + A[start]) or self.canReach(A, start - A[start])
        return False